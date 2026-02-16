import logging
from apps.sarita_agents.agents.coronel_template import CoronelTemplate

class CoronelOperativoAgencia(CoronelTemplate):
    """
    Gobierna la consolidación de Paquetes Turísticos y Agencias de Viajes.
    """
    def __init__(self, general):
        super().__init__(general=general, domain="operativo_agencia")

    def _get_capitanes(self) -> dict:
        from .capitanes.capitan_agencia import CapitanAgencia
        return {
            "agencia": CapitanAgencia(coronel=self),
        }

    def _select_capitan(self, directiva: dict):
        return self.capitanes.get("agencia")
