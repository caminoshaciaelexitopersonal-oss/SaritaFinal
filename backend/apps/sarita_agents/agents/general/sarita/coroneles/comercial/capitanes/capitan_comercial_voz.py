# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import CapitanComercialBase

logger = logging.getLogger(__name__)

class CapitanComercialVoz(CapitanComercialBase):
    nivel = "CAPITAN"
    dominio = "GESTION_COMERCIAL"
    superior = "CoronelComercialGeneral"
    mision = "Gobernar el dominio comercial de comercial_voz"
    eventos = ['mision_planificada']
    dependencias = []
