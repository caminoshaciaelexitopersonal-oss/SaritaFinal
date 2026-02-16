import logging
from apps.sarita_agents.agents.coronel_template import CoronelTemplate

class CoronelOperativoArtesanos(CoronelTemplate):
    """
    Gobierna la operación especializada de Talleres y Producción Artesanal.
    """
    def __init__(self, general):
        super().__init__(general=general, domain="operativo_artesano")

    def _get_capitanes(self) -> dict:
        from .capitanes.capitan_taller import CapitanTaller
        return {
            "taller": CapitanTaller(coronel=self),
        }

    def _select_capitan(self, directiva: dict):
        return self.capitanes.get("taller")
