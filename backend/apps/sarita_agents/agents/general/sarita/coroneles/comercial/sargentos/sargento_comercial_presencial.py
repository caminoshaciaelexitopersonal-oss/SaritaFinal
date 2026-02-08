# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoComercialPresencial(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteComercialPresencial"
    mision = "Ejecutar acción atómica de comercial_presencial"
    eventos = ['accion_completada']
    dependencias = []
