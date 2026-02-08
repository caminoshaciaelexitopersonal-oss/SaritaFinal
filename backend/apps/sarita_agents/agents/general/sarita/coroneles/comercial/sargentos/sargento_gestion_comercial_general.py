# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoGestionComercialGeneral(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteGestionComercialGeneral"
    mision = "Ejecutar acción atómica de gestion_comercial_general"
    eventos = ['accion_completada']
    dependencias = []
