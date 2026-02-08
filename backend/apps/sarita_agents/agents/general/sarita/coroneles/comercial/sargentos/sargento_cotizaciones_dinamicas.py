# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoCotizacionesDinamicas(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteCotizacionesDinamicas"
    mision = "Ejecutar acción atómica de cotizaciones_dinamicas"
    eventos = ['accion_completada']
    dependencias = []
