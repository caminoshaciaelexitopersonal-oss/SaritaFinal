# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteComercialArtesanos(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanComercialArtesanos"
    mision = "Planificar tácticamente comercial_artesanos"
    eventos = ['tactica_definida']
    dependencias = []
