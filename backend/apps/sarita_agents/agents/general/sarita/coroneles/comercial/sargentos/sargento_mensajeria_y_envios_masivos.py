# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoMensajeriaYEnviosMasivos(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteMensajeriaYEnviosMasivos"
    mision = "Ejecutar acción atómica de mensajeria_y_envios_masivos"
    eventos = ['accion_completada']
    dependencias = []
