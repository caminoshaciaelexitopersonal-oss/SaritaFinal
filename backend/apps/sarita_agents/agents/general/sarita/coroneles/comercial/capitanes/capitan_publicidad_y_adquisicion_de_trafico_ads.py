# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import CapitanComercialBase

logger = logging.getLogger(__name__)

class CapitanPublicidadYAdquisicionDeTraficoAds(CapitanComercialBase):
    nivel = "CAPITAN"
    dominio = "GESTION_COMERCIAL"
    superior = "CoronelComercialGeneral"
    mision = "Gobernar el dominio comercial de publicidad_y_adquisicion_de_trafico_ads"
    eventos = ['mision_planificada']
    dependencias = []
