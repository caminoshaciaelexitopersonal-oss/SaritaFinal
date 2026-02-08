# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoComercialAgencias(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteComercialAgencias"
    mision = "Ejecutar acción atómica de comercial_agencias"
    eventos = ['accion_completada']
    dependencias = []
