import logging
from django.shortcuts import get_object_or_404
from django.db import transaction
from .models import DeliveryCompany, Driver, Vehicle, DeliveryService, DeliveryEvent
from api.models import CustomUser
from apps.wallet.services import WalletService
from apps.wallet.models import WalletAccount

logger = logging.getLogger(__name__)

class DeliveryLogisticService:
    def __init__(self, user: CustomUser):
        self.user = user

    def create_request(self, parameters, intention_id=None):
        with transaction.atomic():
            service = DeliveryService.objects.create(
                tourist=self.user,
                origin_address=parameters["origin_address"],
                destination_address=parameters["destination_address"],
                estimated_price=parameters["estimated_price"],
                governance_intention_id=intention_id,
                status=DeliveryService.Status.REQUESTED
            )

            DeliveryEvent.objects.create(
                service=service,
                event_type="REQUEST_CREATED",
                description=f"Servicio solicitado por {self.user.username}"
            )

            return service

    def assign_service(self, parameters):
        service = get_object_or_404(DeliveryService, id=parameters["service_id"])
        driver = get_object_or_404(Driver, id=parameters["driver_id"])
        vehicle = get_object_or_404(Vehicle, id=parameters["vehicle_id"])

        with transaction.atomic():
            service.driver = driver
            service.vehicle = vehicle
            service.delivery_company = driver.delivery_company
            service.status = DeliveryService.Status.ASSIGNED
            service.save()

            DeliveryEvent.objects.create(
                service=service,
                event_type="DRIVER_ASSIGNED",
                description=f"Conductor {driver.user.username} asignado con vehículo {vehicle.plate}"
            )

            return service

    def complete_service(self, service_id):
        service = get_object_or_404(DeliveryService, id=service_id)

        if service.status == DeliveryService.Status.COMPLETED:
            return service

        with transaction.atomic():
            service.status = DeliveryService.Status.COMPLETED
            service.final_price = service.estimated_price # Por ahora igual
            service.save()

            DeliveryEvent.objects.create(
                service=service,
                event_type="SERVICE_COMPLETED",
                description="Servicio finalizado exitosamente."
            )

            # --- INTEGRACIÓN CON MONEDERO (PAGO OBLIGATORIO) ---
            self._process_payment(service)

            return service

    def _process_payment(self, service):
        """
        Ejecuta el pago real desde el monedero del turista al monedero de la empresa/conductor.
        """
        wallet_service = WalletService(user=service.tourist)

        # Obtenemos la cartera de destino (Empresa de Delivery)
        # Asumimos que la empresa tiene una WalletAccount
        try:
            target_wallet = WalletAccount.objects.get(
                user=service.delivery_company.company.user if hasattr(service.delivery_company.company, 'user') else service.driver.user
            )
        except WalletAccount.DoesNotExist:
            # Fallback a la cartera del conductor si la empresa no tiene una centralizada
            target_wallet = WalletAccount.objects.get(user=service.driver.user)

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
