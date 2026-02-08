# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoConversion(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteConversion"
    mision = "Ejecutar acción atómica de conversion"
    eventos = ['accion_completada']
    dependencias = []
