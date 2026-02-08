# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoComercialGastronomico(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteComercialGastronomico"
    mision = "Ejecutar acción atómica de comercial_gastronomico"
    eventos = ['accion_completada']
    dependencias = []
