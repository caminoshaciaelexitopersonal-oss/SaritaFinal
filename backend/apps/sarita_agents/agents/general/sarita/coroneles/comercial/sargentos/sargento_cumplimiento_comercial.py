# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoCumplimientoComercial(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteCumplimientoComercial"
    mision = "Ejecutar acción atómica de cumplimiento_comercial"
    eventos = ['accion_completada']
    dependencias = []
