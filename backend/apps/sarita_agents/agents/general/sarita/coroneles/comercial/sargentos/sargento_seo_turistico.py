# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoSeoTuristico(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteSeoTuristico"
    mision = "Ejecutar acción atómica de seo_turistico"
    eventos = ['accion_completada']
    dependencias = []
