import logging
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from .models import (
    NightEvent, NightConsumption, NightConsumptionItem,
    LiquorInventory, InventoryMovement, CashClosing, EventLiquidation
)
from apps.admin_plataforma.services.quintuple_erp import QuintupleERPService

logger = logging.getLogger(__name__)

class NightclubService:
    """
    Motor Operativo para Bares y Discotecas (Fase 11)
    """
    def __init__(self, user):
        self.user = user
        self.provider = user.perfil_prestador

    @transaction.atomic
    def registrar_consumo(self, consumption_id, items_data):
        """
        Registra items en un consumo y descuenta inventario.
        """
        consumption = NightConsumption.objects.select_for_update().get(id=consumption_id, provider=self.provider)

        if consumption.estado != NightConsumption.ConsumptionStatus.ABIERTO:
            raise ValueError("El consumo no está abierto.")

        for item in items_data:
            product_id = item['product_id']
            cantidad = Decimal(str(item['cantidad']))

            # 1. Verificar inventario
            liquor = LiquorInventory.objects.select_for_update().get(product_id=product_id, provider=self.provider)
            if liquor.stock_actual < cantidad:
                raise ValueError(f"Stock insuficiente para {liquor.product.nombre}")

            # 2. Descontar stock
            liquor.stock_actual -= cantidad
            liquor.save()

            # 3. Registrar movimiento
            InventoryMovement.objects.create(
                liquor=liquor,
                tipo=InventoryMovement.MovementType.SALIDA_CONSUMO,
                cantidad=cantidad,
                referencia_consumo=consumption,
                usuario=self.user,
                provider=self.provider
            )

            # 4. Crear item de consumo
            NightConsumptionItem.objects.create(
                consumption=consumption,
                product_id=product_id,
                cantidad=cantidad,
                precio_unitario=liquor.product.base_price.amount,
                subtotal=liquor.product.base_price.amount * cantidad
            )

        # 5. Recalcular totales del consumo
        self._recalculate_consumption(consumption)
        return consumption

    def _recalculate_consumption(self, consumption):
        total_data = consumption.items.aggregate(
            subtotal=models.Sum('subtotal')
        )
        consumption.subtotal = total_data['subtotal'] or Decimal('0.00')
        # Supuesto: IVA 19%
        consumption.impuestos = consumption.subtotal * Decimal('0.19')
        consumption.total = consumption.subtotal + consumption.impuestos
        consumption.save()

    @transaction.atomic
    def facturar_consumo(self, consumption_id):
        """
        Cierra el consumo y dispara el impacto en el ERP Quíntuple.
        """
        consumption = NightConsumption.objects.select_for_update().get(id=consumption_id, provider=self.provider)

        if consumption.estado != NightConsumption.ConsumptionStatus.ABIERTO:
            raise ValueError("El consumo ya ha sido procesado.")

        consumption.estado = NightConsumption.ConsumptionStatus.FACTURADO
        consumption.fecha_cierre = timezone.now()
        consumption.save()

        # IMPACTO ERP (Vía 2 - Comercial & Contable)
        erp_service = QuintupleERPService(user=self.user)
        payload = {
            "perfil_id": str(self.provider.id),
            "amount": float(consumption.total),
            "description": f"Consumo Discoteca #{consumption.id}",
            "cliente_id": str(consumption.cliente_ref_id) if consumption.cliente_ref_id else None
        }

        # Esto genera Factura + Asiento Contable + Registro Archivístico
        impact = erp_service.record_impact("NIGHT_CONSUMPTION", payload)

        return impact

    @transaction.atomic
    def cierre_caja(self, event_id, data):
        """
        Realiza el cierre de caja de un evento.
        """
        event = NightEvent.objects.get(id=event_id, provider=self.provider)

        closing = CashClosing.objects.create(
            evento=event,
            staff_cierre=self.user,
            total_efectivo=data.get('efectivo', 0),
            total_tarjeta=data.get('tarjeta', 0),
            total_monedero=data.get('monedero', 0),
            total_real=data.get('total_real', 0),
            provider=self.provider
        )

        # Calcular esperado basado en consumos facturados
        total_facturado = NightConsumption.objects.filter(
            evento=event,
            estado__in=[NightConsumption.ConsumptionStatus.FACTURADO, NightConsumption.ConsumptionStatus.PAGADO]
        ).aggregate(t=models.Sum('total'))['t'] or 0

        closing.total_esperado = total_facturado
        closing.diferencia = closing.total_real - closing.total_esperado
        closing.save()

        return closing

from django.db import models # Añadido para los agregados
