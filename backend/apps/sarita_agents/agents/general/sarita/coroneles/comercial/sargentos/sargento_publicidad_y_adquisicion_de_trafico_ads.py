# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoPublicidadYAdquisicionDeTraficoAds(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenientePublicidadYAdquisicionDeTraficoAds"
    mision = "Ejecutar acción atómica de publicidad_y_adquisicion_de_trafico_ads"
    eventos = ['accion_completada']
    dependencias = []
