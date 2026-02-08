# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteGestionComercialGeneral(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanGestionComercialGeneral"
    mision = "Planificar tácticamente gestion_comercial_general"
    eventos = ['tactica_definida']
    dependencias = []
