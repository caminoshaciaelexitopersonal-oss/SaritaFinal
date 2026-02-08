# backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial/dominios/conversion/sargentos/sargento_validacion_precio.py

from .......sargento_template import SargentoTemplate
from decimal import Decimal

class SargentoValidacionPrecio(SargentoTemplate):
    """
    Sargento de Validación de Precio.
    Función atómica: Verificar que el precio propuesto cumple con los rangos permitidos.
    """
    def perform_atomic_action(self, action_data: dict):
        precio = Decimal(str(action_data.get("precio", 0)))
        min_price = Decimal(str(action_data.get("min_allowed", 0)))
        max_price = Decimal(str(action_data.get("max_allowed", 999999999)))

        if precio < min_price:
            raise ValueError(f"Precio {precio} por debajo del mínimo permitido {min_price}")
        if precio > max_price:
            raise ValueError(f"Precio {precio} por encima del máximo permitido {max_price}")

        return {"validated": True, "precio": float(precio)}
