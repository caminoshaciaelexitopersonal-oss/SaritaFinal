# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoPrevencionFraude(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenientePrevencionFraude"
    mision = "Ejecutar acción atómica de prevencion_fraude"
    eventos = ['accion_completada']
    dependencias = []
