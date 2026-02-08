# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoPostventaFeedback(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenientePostventaFeedback"
    mision = "Ejecutar acción atómica de postventa_feedback"
    eventos = ['accion_completada']
    dependencias = []
