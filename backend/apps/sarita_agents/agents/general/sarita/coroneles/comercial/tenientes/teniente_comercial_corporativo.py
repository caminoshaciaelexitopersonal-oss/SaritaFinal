# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteComercialCorporativo(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanComercialCorporativo"
    mision = "Planificar tácticamente comercial_corporativo"
    eventos = ['tactica_definida']
    dependencias = []
