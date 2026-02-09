import logging
from .models import InventoryItem
logger = logging.getLogger(__name__)
class InventarioService:
    @staticmethod
    def update_stock(item_id, change):
        item = InventoryItem.objects.get(id=item_id)
        item.cantidad += change
        item.save()
        logger.info(f"Inventario actualizado: {item.nombre_item} (Nueva cant: {item.cantidad})")
