import logging
from apps.sarita_agents.agents.coronel_template import CoronelTemplate

class CoronelOperativoGuias(CoronelTemplate):
    """
    Gobierna la operación especializada de Guías Turísticos (Fase 12).
    """
    def __init__(self, general):
        super().__init__(general=general, domain="operativo_guias")

    def _get_capitanes(self) -> dict:
        from .capitanes.capitan_gestion_guias import CapitanGestionGuias
        return {
            "gestion_guias": CapitanGestionGuias(coronel=self),
        }

    def _select_capitan(self, directiva: dict):
        return self.capitanes.get("gestion_guias")
