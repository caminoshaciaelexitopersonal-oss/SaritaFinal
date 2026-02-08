# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoComercialArtesanos(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteComercialArtesanos"
    mision = "Ejecutar acción atómica de comercial_artesanos"
    eventos = ['accion_completada']
    dependencias = []
