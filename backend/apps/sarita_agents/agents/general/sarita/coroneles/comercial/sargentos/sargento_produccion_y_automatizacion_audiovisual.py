# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoProduccionYAutomatizacionAudiovisual(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteProduccionYAutomatizacionAudiovisual"
    mision = "Ejecutar acción atómica de produccion_y_automatizacion_audiovisual"
    eventos = ['accion_completada']
    dependencias = []
