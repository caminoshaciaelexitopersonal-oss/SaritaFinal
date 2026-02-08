# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteComercialEstrategico(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanComercialEstrategico"
    mision = "Planificar tácticamente comercial_estrategico"
    eventos = ['tactica_definida']
    dependencias = []
