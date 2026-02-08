# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteComercialGastronomico(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanComercialGastronomico"
    mision = "Planificar tácticamente comercial_gastronomico"
    eventos = ['tactica_definida']
    dependencias = []
