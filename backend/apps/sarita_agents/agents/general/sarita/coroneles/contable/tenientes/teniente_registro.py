# backend/apps/sarita_agents/agents/general/sarita/coroneles/contable/tenientes/teniente_registro.py

from apps.sarita_agents.agents.teniente_template import TenienteTemplate
from ..sargentos.sargento_asientos import SargentoAsientosContables
import logging

logger = logging.getLogger(__name__)

class TenienteRegistroContable(TenienteTemplate):
    """
    NIVEL 4 — TENIENTE DE REGISTRO
    Supervisa tareas concretas y controla la consistencia de datos.
    """
    def perform_action(self, parametros: dict) -> dict:
        logger.info(f"TENIENTE REGISTRO: Validando consistencia de datos contables.")

        # Delegación al Sargento de Asientos
        sargento = SargentoAsientosContables(teniente=self)
        sargento_report = sargento.handle_order(parametros)

        return {
            "status": "SUCCESS",
            "message": "Validación técnica completada por Teniente.",
            "sargento_report": sargento_report
        }
