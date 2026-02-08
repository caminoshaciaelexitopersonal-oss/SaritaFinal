# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteMensajeriaYEnviosMasivos(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanMensajeriaYEnviosMasivos"
    mision = "Planificar tácticamente mensajeria_y_envios_masivos"
    eventos = ['tactica_definida']
    dependencias = []
