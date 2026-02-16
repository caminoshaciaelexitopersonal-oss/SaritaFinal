# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/tenientes/operativo_artesano_teniente.py

from apps.sarita_agents.agents.teniente_template import TenienteTemplate
from ..sargentos.sargento_artesano import SargentoGestionTallerArtesano
import logging

logger = logging.getLogger(__name__)

class TenienteOperativoArtesano(TenienteTemplate):
    def perform_action(self, parametros: dict) -> dict:
        logger.info(f"TENIENTE ARTESANO: Iniciando ejecución coordinada del taller.")

        sargento = SargentoGestionTallerArtesano(teniente=self)
        sargento_report = sargento.handle_order(parametros)

        return {
            "status": "SUCCESS",
            "message": "Operación de taller artesano coordinada.",
            "sargento_report": sargento_report
        }
