# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenientePublicidadYAdquisicionDeTraficoAds(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanPublicidadYAdquisicionDeTraficoAds"
    mision = "Planificar tácticamente publicidad_y_adquisicion_de_trafico_ads"
    eventos = ['tactica_definida']
    dependencias = []
