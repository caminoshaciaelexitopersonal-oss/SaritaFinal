# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoRecomendacionesSadi(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteRecomendacionesSadi"
    mision = "Ejecutar acción atómica de recomendaciones_sadi"
    eventos = ['accion_completada']
    dependencias = []
