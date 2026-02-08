# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoEmbudosConversion(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteEmbudosConversion"
    mision = "Ejecutar acción atómica de embudos_conversion"
    eventos = ['accion_completada']
    dependencias = []
