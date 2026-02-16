import logging
from apps.sarita_agents.agents.coronel_template import CoronelTemplate

class CoronelOperativoNocturno(CoronelTemplate):
    """
    Gobierna la operación especializada de Bares y Discotecas (Fase 11).
    """
    def __init__(self, general):
        super().__init__(general=general, domain="operativo_nocturno")

    def _get_capitanes(self) -> dict:
        from .capitanes.capitan_operacion_nocturna import CapitanOperacionNocturna
        return {
            "operacion_nocturna": CapitanOperacionNocturna(coronel=self),
        }

    def _select_capitan(self, directiva: dict):
        return self.capitanes.get("operacion_nocturna")
