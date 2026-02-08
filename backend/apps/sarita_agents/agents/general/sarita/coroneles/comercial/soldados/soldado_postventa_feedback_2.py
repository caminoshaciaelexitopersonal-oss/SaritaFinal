# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SoldadoComercialBase

logger = logging.getLogger(__name__)

class SoldadoPostventaFeedback2(SoldadoComercialBase):
    nivel = "SOLDADO"
    dominio = "GESTION_COMERCIAL"
    superior = "SargentoPostventaFeedback"
    mision = "Ejecución manual paso 2 para postventa_feedback"
    eventos = ['tarea_manual_realizada']
    dependencias = []
