import logging
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from .models import (
    TravelPackage, PackageComponent, AgencyBooking,
    AgencyLiquidation, ProviderCommission, PackageIncident
)
from apps.admin_plataforma.services.quintuple_erp import QuintupleERPService

logger = logging.getLogger(__name__)

class AgencyService:
    """
    Motor de Consolidación para Agencias de Viajes (Fase 14)
    """
    def __init__(self, user):
        self.user = user
        self.provider = user.perfil_prestador

    @transaction.atomic
    def crear_paquete(self, data):
        """
        Crea un paquete turístico unificando múltiples servicios.
        """
        package = TravelPackage.objects.create(
            provider=self.provider,
            nombre=data['nombre'],
            descripcion=data['descripcion'],
            margen_agencia=data.get('margen_agencia', 10.0),
            duracion_dias=data.get('duracion_dias', 1),
            estado=TravelPackage.PackageStatus.BORRADOR
        )

        componentes_data = data.get('componentes', [])
        total_acumulado = Decimal('0.00')

        for comp in componentes_data:
            componente = PackageComponent.objects.create(
                package=package,
                tipo_servicio=comp['tipo_servicio'],
                proveedor_id=comp['proveedor_id'],
                referencia_id=comp['referencia_id'],
                precio_proveedor=Decimal(str(comp['precio_proveedor'])),
                comision_proveedor=Decimal(str(comp.get('comision_proveedor', 0)))
            )
            total_acumulado += componente.precio_proveedor

        # El precio total incluye el margen de la agencia
        margen_dec = Decimal(str(package.margen_agencia))
        factor_margen = Decimal('1') + (margen_dec / Decimal('100'))
        package.precio_total = total_acumulado * factor_margen
        package.save()

        return package

    @transaction.atomic
    def registrar_reserva_paquete(self, package_id, data_reserva):
        """
        Reserva un paquete consolidado (Fase 14.1.5).
        """
        package = TravelPackage.objects.select_for_update().get(id=package_id, provider=self.provider)

        if package.estado not in [TravelPackage.PackageStatus.PUBLICADO, TravelPackage.PackageStatus.BORRADOR]:
            # Permitimos BORRADOR para pruebas, pero en producción debería ser PUBLICADO
            pass

        n_personas = int(data_reserva['numero_personas'])
        total_pago = package.precio_total * n_personas

        booking = AgencyBooking.objects.create(
            provider=self.provider,
            package=package,
            cliente_ref_id=data_reserva['cliente_ref_id'],
            fecha_inicio=data_reserva['fecha_inicio'],
            numero_personas=n_personas,
            total_facturado=total_pago,
            status=AgencyBooking.BookingStatus.CONFIRMED
        )

        # IMPACTO ERP (Consolidado)
        erp_service = QuintupleERPService(user=self.user)
        impact = erp_service.record_impact("AGENCY_PACKAGE_BOOKING", {
            "booking_id": str(booking.id),
            "amount": float(total_pago),
            "description": f"Reserva Paquete: {package.nombre}"
        })

        booking.asiento_contable_id = impact.get('contable_id')
        booking.save()

        return booking

    @transaction.atomic
    def cancelar_componente_parcial(self, booking_id, component_id):
        from decimal import Decimal
        """
        Ruptura controlada: Cancelación de un componente específico (Fase 14.2.2).
        """
        booking = AgencyBooking.objects.select_for_update().get(id=booking_id, provider=self.provider)
        component = PackageComponent.objects.get(id=component_id, package=booking.package)

        if not component.is_active:
            raise ValueError("El componente ya está inactivo.")

        # 1. Desactivar componente
        component.is_active = False
        component.save()

        # 2. Recalcular precio de la reserva
        margen_dec = Decimal(str(booking.package.margen_agencia))
        factor = Decimal('1') + (margen_dec / Decimal('100'))
        valor_a_descontar = component.precio_proveedor * factor
        booking.total_facturado -= valor_a_descontar * booking.numero_personas
        booking.save()

        # 3. Registrar incidencia
        PackageIncident.objects.create(
            provider=self.provider,
            package=booking.package,
            booking=booking,
            descripcion=f"Cancelación parcial de componente: {component.tipo_servicio}",
            nivel_gravedad='MEDIUM'
        )

        # 4. Impacto ERP (Nota Crédito / Ajuste)
        erp_service = QuintupleERPService(user=self.user)
        erp_service.record_impact("AGENCY_BOOKING_ADJUSTMENT", {
            "booking_id": str(booking.id),
            "amount_adjusted": float(-valor_a_descontar * booking.numero_personas),
            "reason": "Partial component cancellation"
        })

        return booking

    @transaction.atomic
    def liquidar_paquete(self, booking_id):
        """
        Distribución de comisiones y liquidación final (Fase 14.1.6).
        """
        booking = AgencyBooking.objects.select_for_update().get(id=booking_id, provider=self.provider)

        if hasattr(booking, 'liquidation'):
            raise ValueError("Este paquete ya ha sido liquidado.")

        total_costo = Decimal('0.00')
        componentes_activos = booking.package.components.filter(is_active=True)

        # Verificación de consistencia (Fase 14.3.4)
        suma_componentes = sum(c.precio_proveedor for c in componentes_activos) * booking.numero_personas
        margen_dec = Decimal(str(booking.package.margen_agencia))
        factor = Decimal('1') + (margen_dec / Decimal('100'))
        total_esperado = suma_componentes * factor

        if abs(total_esperado - booking.total_facturado) > Decimal('0.01'):
            raise ValueError(f"Inconsistencia financiera detectada. Descuadre entre componentes y factura.")

        liq = AgencyLiquidation.objects.create(
            provider=self.provider,
            booking=booking,
            monto_total_ingresado=booking.total_facturado,
            total_costo_proveedores=0, # Se actualiza abajo
            utilidad_agencia=0 # Se actualiza abajo
        )

        for comp in componentes_activos:
            costo_unitario = comp.precio_proveedor
            costo_total_comp = costo_unitario * booking.numero_personas
            comision = comp.comision_proveedor * booking.numero_personas

            ProviderCommission.objects.create(
                liquidation=liq,
                proveedor=comp.proveedor,
                monto_base=costo_total_comp,
                monto_comision=comision
            )
            total_costo += costo_total_comp

        liq.total_costo_proveedores = total_costo
        liq.utilidad_agencia = liq.monto_total_ingresado - total_costo
        liq.procesado = True
        liq.save()

        # Marcar paquete como liquidado si es la única reserva o según lógica de negocio
        booking.package.estado = TravelPackage.PackageStatus.LIQUIDADO
        booking.package.save()

        return liq
