import logging
from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.db import transaction
from .models import DeliveryCompany, Driver, Vehicle, DeliveryService, DeliveryEvent
from api.models import CustomUser
from apps.wallet.services import WalletService
from apps.wallet.models import WalletAccount

logger = logging.getLogger(__name__)

class LogisticService:
    """ Motor Logístico SARITA (Fase 9) """
    def __init__(self, user: CustomUser = None):
        self.user = user

    def create_request(self, parameters, intention_id=None):
        with transaction.atomic():
            service = DeliveryService.objects.create(
                tourist=self.user,
                origin_address=parameters["origin_address"],
                destination_address=parameters["destination_address"],
                estimated_price=parameters.get("estimated_price", 0),
                governance_intention_id=intention_id,
                status=DeliveryService.Status.PENDIENTE,
                related_operational_order_id=parameters.get("related_operational_order_id"),
                provider_id=parameters.get("provider_id"),
                prioridad=parameters.get("prioridad", "NORMAL")
            )

            DeliveryEvent.objects.create(
                service=service,
                event_type="REQUEST_CREATED",
                description=f"Pedido de delivery creado."
            )

            # --- IMPACTO ERP QUÍNTUPLE (FASE 9) ---
            self._propagate_erp_impact(service, "DELIVERY_REQUESTED")

            return service

    def assign_service(self, service_id, driver_id=None):
        service = get_object_or_404(DeliveryService, id=service_id)

        # Asignación Automática si no viene driver_id
        if not driver_id:
            driver = Driver.objects.filter(is_available=True).first()
            if not driver:
                raise ValueError("No hay repartidores disponibles en este momento.")
        else:
            driver = get_object_or_404(Driver, id=driver_id)

        vehicle = Vehicle.objects.filter(delivery_company=driver.delivery_company, is_active=True).first()

        with transaction.atomic():
            service.driver = driver
            service.vehicle = vehicle
            service.delivery_company = driver.delivery_company
            service.status = DeliveryService.Status.LISTO_DESPACHO
            service.save()

            driver.is_available = False
            driver.save()

            DeliveryEvent.objects.create(
                service=service,
                event_type="ASSIGNED",
                description=f"Repartidor {driver.user.username} asignado."
            )

            self._propagate_erp_impact(service, "DELIVERY_ASSIGNED")

            return service

    def start_delivery(self, service_id):
        service = get_object_or_404(DeliveryService, id=service_id)
        service.status = DeliveryService.Status.EN_RUTA
        service.save()

        DeliveryEvent.objects.create(service=service, event_type="IN_ROUTE", description="Pedido en ruta.")
        return service

    def fail_delivery(self, service_id, reason):
        service = get_object_or_404(DeliveryService, id=service_id)
        service.status = DeliveryService.Status.FALLIDO
        service.save()

        DeliveryEvent.objects.create(service=service, event_type="FAILED", description=f"Falla: {reason}")
        return service

    def complete_service(self, service_id, parameters=None):
        service = get_object_or_404(DeliveryService, id=service_id)

        if service.status == DeliveryService.Status.ENTREGADO:
            return service

        with transaction.atomic():
            service.status = DeliveryService.Status.ENTREGADO
            service.final_price = service.estimated_price
            # Cálculo de Comisión Repartidor (15% por defecto para Fase 9)
            service.comision_repartidor = service.final_price * Decimal('0.15')
            service.save()

            if parameters:
                from .models import EvidenciaEntrega
                EvidenciaEntrega.objects.create(
                    delivery=service,
                    firma_digital=parameters.get("firma", ""),
                    observaciones=parameters.get("observaciones", ""),
                    latitud=parameters.get("latitud"),
                    longitud=parameters.get("longitud")
                )

            DeliveryEvent.objects.create(
                service=service,
                event_type="COMPLETED",
                description="Entrega confirmada."
            )

            if service.driver:
                service.driver.is_available = True
                service.driver.save()

            # --- INTEGRACIÓN CON MONEDERO (PAGO OBLIGATORIO) ---
            self._process_payment(service)
            self._propagate_erp_impact(service, "DELIVERY_COMPLETED")

            return service

    def rate_service(self, service_id, rating, comment=""):
        service = get_object_or_404(DeliveryService, id=service_id)
        if service.status != DeliveryService.Status.COMPLETED:
            raise ValueError("Solo se pueden calificar servicios completados.")

        service.rating = rating
        service.tourist_comment = comment
        service.save()

        logger.info(f"DELIVERY: Servicio {service_id} calificado con {rating}")
        return service

    def _propagate_erp_impact(self, service, event_type):
        """Propaga el impacto a las 5 dimensiones del ERP."""
        from apps.admin_plataforma.services.quintuple_erp import QuintupleERPService
        erp_service = QuintupleERPService(user=self.user)

        payload = {
            "company_id": str(service.delivery_company.company.id) if (service.delivery_company and service.delivery_company.company) else None,
            "perfil_id": str(service.provider_id) if service.provider_id else None,
            "cliente_id": str(service.tourist.id),
            "amount": float(service.final_price or service.estimated_price),
            "description": f"Servicio Delivery {service.id} - {event_type}",
            "delivery_service_id": str(service.id),
            "reserva_id": str(service.related_operational_order_id) if service.related_operational_order_id else None,
            "wallet_transaction_id": str(service.wallet_transaction) if service.wallet_transaction else None
        }

        erp_service.record_impact(event_type, payload)

    def _process_payment(self, service):
        """
        Ejecuta el pago real desde el monedero del turista al monedero de la empresa/conductor.
        """
        wallet_service = WalletService(user=service.tourist)

        # Determinar el usuario receptor (Preferimos al conductor en Fase 9 por simplicidad de mapeo)
        target_user = None
        if service.driver:
            target_user = service.driver.user

        if not target_user:
            logger.warning(f"PAGO DELIVERY: No se puede procesar pago sin receptor asignado en servicio {service.id}")
            return

        try:
            target_wallet = WalletAccount.objects.get(user=target_user)
        except WalletAccount.DoesNotExist:
            logger.error(f"PAGO DELIVERY: Receptor {target_user.username} no tiene monedero.")
            return

        # Ejecutar pago via monedero gobernado
        tx_result = wallet_service.pay(
            to_wallet_id=str(target_wallet.id),
            amount=service.final_price,
            related_service_id=service.id,
            description=f"Pago por servicio de Delivery {service.id}"
        )

        service.wallet_transaction = tx_result.id
        service.save()

        logger.info(f"PAGO DELIVERY: Procesado para servicio {service.id} via TX {tx_result.id}")

    @staticmethod
    def generar_indicadores(provider_id):
        """ Genera KPIs de Delivery para un Tenant """
        from .models import IndicadorLogistico, DeliveryService
        from django.db.models import Avg, Count, F, Sum
        from django.utils import timezone

        periodo = timezone.now().strftime("%Y-%m")

        # 1. Tiempo Promedio de Entrega (Simulado para Fase 9 ya que no guardamos timestamps exactos de hitos en campos de tiempo)
        # En producción se usaría la diferencia entre IN_ROUTE y COMPLETED

        # 2. Total Entregas
        total = DeliveryService.objects.filter(provider_id=provider_id, status=DeliveryService.Status.ENTREGADO).count()
        IndicadorLogistico.objects.create(provider_id=provider_id, nombre="Entregas Exitosas", valor=total, periodo=periodo)

        # 3. Costo Logístico (Suma de comisiones)
        costo = DeliveryService.objects.filter(provider_id=provider_id, status=DeliveryService.Status.ENTREGADO).aggregate(s=Sum('comision_repartidor'))['s'] or 0
        IndicadorLogistico.objects.create(provider_id=provider_id, nombre="Costo Logístico Total", valor=costo, periodo=periodo)

        return True
