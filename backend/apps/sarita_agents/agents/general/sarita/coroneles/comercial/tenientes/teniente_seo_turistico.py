# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteSeoTuristico(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanSeoTuristico"
    mision = "Planificar tácticamente seo_turistico"
    eventos = ['tactica_definida']
    dependencias = []
