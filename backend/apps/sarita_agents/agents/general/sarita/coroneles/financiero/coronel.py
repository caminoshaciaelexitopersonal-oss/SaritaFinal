# backend/apps/sarita_agents/agents/general/sarita/coroneles/financiero/coronel.py

from .....coronel_template import CoronelTemplate
from .capitanes.capitan_financiero import CapitanFinanciero

class CoronelFinanciero(CoronelTemplate):
    """
    NIVEL 2 — CORONEL FINANCIERO
    Gobierno de recursos monetarios, proyecciones y cumplimiento de metas de rentabilidad.
    """
    def __init__(self, general):
        super().__init__(general=general, domain="finanzas")

    def _get_capitanes(self) -> dict:
        return {
            "financiero_general": CapitanFinanciero(coronel=self)
        }

    def _select_capitan(self, directiva: dict):
        return self.capitanes.get("financiero_general")
