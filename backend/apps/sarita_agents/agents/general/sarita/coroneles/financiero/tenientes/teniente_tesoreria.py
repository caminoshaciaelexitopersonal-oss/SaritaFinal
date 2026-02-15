# backend/apps/sarita_agents/agents/general/sarita/coroneles/financiero/tenientes/teniente_tesoreria.py

from apps.sarita_agents.agents.teniente_template import TenienteTemplate
from ..sargentos.sargento_finanzas import SargentoFinanzas
import logging

logger = logging.getLogger(__name__)

class TenienteTesoreria(TenienteTemplate):
    """
    NIVEL 4 — TENIENTE DE TESORERÍA
    Controla el flujo de caja y la consistencia de los indicadores financieros.
    """
    def perform_action(self, parametros: dict) -> dict:
        logger.info(f"TENIENTE TESORERÍA: Analizando flujos y proyecciones.")
        sargento = SargentoFinanzas(teniente=self)
        return sargento.handle_order(parametros)
