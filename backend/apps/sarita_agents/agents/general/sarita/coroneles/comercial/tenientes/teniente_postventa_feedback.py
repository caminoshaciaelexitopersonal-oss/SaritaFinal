# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenientePostventaFeedback(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanPostventaFeedback"
    mision = "Planificar tácticamente postventa_feedback"
    eventos = ['tactica_definida']
    dependencias = []
