import logging
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import transaction

logger = logging.getLogger(__name__)

class InventoryEngine:
    """
    Motor de inventarios centralizado.
    Gestiona existencias y valoración de stock (Kardex).
    """

    @staticmethod
    def validate_stock_availability(product, warehouse, requested_quantity):
        # Lógica para verificar stock en modelos que hereden de BaseWarehouse e InventoryMovement
        pass

    @staticmethod
    @transaction.atomic
    def record_movement(product, warehouse, quantity, movement_type, description=""):
        """
        Registra un movimiento de entrada o salida.
        """
        if quantity <= 0:
            raise ValidationError("La cantidad del movimiento debe ser positiva.")

        # Aquí se crearía el registro real de InventoryMovement
        logger.info(f"Movimiento de inventario [{movement_type}] para {product}: {quantity}")
        return True
