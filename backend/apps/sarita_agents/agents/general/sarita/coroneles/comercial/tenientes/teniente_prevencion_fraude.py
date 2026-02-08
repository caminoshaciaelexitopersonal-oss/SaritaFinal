# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenientePrevencionFraude(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanPrevencionFraude"
    mision = "Planificar tácticamente prevencion_fraude"
    eventos = ['tactica_definida']
    dependencias = []
