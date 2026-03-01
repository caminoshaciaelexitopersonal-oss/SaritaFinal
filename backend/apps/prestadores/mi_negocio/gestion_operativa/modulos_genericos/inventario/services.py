import logging
from decimal import Decimal
from django.db import transaction
from .models import InventoryItem
logger = logging.getLogger(__name__)
class InventarioService:
    @staticmethod
    @transaction.atomic
    def update_stock(item_id, change, user_id=None, reason="Ajuste Operativo"):
        item = InventoryItem.objects.select_for_update().get(id=item_id)

        # 1. Validación de Disponibilidad
        if change < 0 and item.cantidad < abs(change):
             raise ValueError(f"Stock Insuficiente para {item.nombre_item}. Disponible: {item.cantidad}")

        old_qty = item.cantidad
        item.cantidad += Decimal(str(change))
        item.save()

        # 2. Persistencia en Historial de Movimientos
        from .models import MovimientoInventario
        mov = MovimientoInventario.objects.create(
            producto_id=item_id, # Asumiendo relación o ID directo
            tipo_movimiento='SALIDA' if change < 0 else 'ENTRADA',
            cantidad=abs(change),
            description=reason,
            usuario_id=user_id or 1,
            tenant_id=item.tenant_id
        )

        # 3. Emisión de Evento Contable (Fase 3)
        from apps.core_erp.event_bus import EventBus
        EventBus.emit("INVENTORY_ADJUSTED", {
            "tenant_id": str(item.tenant_id),
            "item_id": str(item.id),
            "change": float(change),
            "reason": reason,
            "cost_impact": 0.0 # TODO: Conectar con motor de costeo real
        })

        logger.info(f"Inventario actualizado: {item.nombre_item} ({old_qty} -> {item.cantidad})")
        return item
