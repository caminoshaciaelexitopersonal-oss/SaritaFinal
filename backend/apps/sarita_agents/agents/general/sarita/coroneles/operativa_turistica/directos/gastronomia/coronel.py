import logging
from apps.sarita_agents.agents.coronel_template import CoronelTemplate

class CoronelOperativoGastronomia(CoronelTemplate):
    """
    Gobierna la operación especializada de Restaurantes y Bares.
    """
    def __init__(self, general):
        super().__init__(general=general, domain="operativo_gastronomia")

    def _get_capitanes(self) -> dict:
        from .capitanes.capitan_servicio_mesa import CapitanServicioMesa
        from .capitanes.capitan_operacion_cocina import CapitanOperacionCocina

        return {
            "servicio_mesa": CapitanServicioMesa(coronel=self),
            "cocina": CapitanOperacionCocina(coronel=self),
        }

    def _select_capitan(self, directiva: dict):
        m_type = directiva.get("mission", {}).get("type")
        mapping = {
            "MANAGE_TABLES": "servicio_mesa",
            "PROCESS_KITCHEN_ORDER": "cocina",
        }
        cap_key = mapping.get(m_type)
        return self.capitanes.get(cap_key) if cap_key else self.capitanes.get("servicio_mesa")
