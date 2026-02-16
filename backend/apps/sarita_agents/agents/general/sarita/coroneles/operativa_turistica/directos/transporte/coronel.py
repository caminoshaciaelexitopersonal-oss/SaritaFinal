import logging
from apps.sarita_agents.agents.coronel_template import CoronelTemplate

class CoronelOperativoTransporte(CoronelTemplate):
    """
    Gobierna la operación especializada de Flotas y Rutas.
    """
    def __init__(self, general):
        super().__init__(general=general, domain="operativo_transporte")

    def _get_capitanes(self) -> dict:
        from .capitanes.capitan_despacho_flota import CapitanDespachoFlota
        from .capitanes.capitan_monitoreo_rutas import CapitanMonitoreoRutas

        return {
            "despacho": CapitanDespachoFlota(coronel=self),
            "monitoreo": CapitanMonitoreoRutas(coronel=self),
        }

    def _select_capitan(self, directiva: dict):
        m_type = directiva.get("mission", {}).get("type")
        mapping = {
            "DISPATCH_VEHICLE": "despacho",
            "UPDATE_ROUTE_PROGRESS": "monitoreo",
        }
        cap_key = mapping.get(m_type)
        return self.capitanes.get(cap_key) if cap_key else self.capitanes.get("despacho")
