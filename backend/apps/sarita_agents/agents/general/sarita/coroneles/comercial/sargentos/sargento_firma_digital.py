# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoFirmaDigital(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteFirmaDigital"
    mision = "Ejecutar acción atómica de firma_digital"
    eventos = ['accion_completada']
    dependencias = []
