# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SoldadoComercialBase

logger = logging.getLogger(__name__)

class SoldadoMensajeriaYEnviosMasivos2(SoldadoComercialBase):
    nivel = "SOLDADO"
    dominio = "GESTION_COMERCIAL"
    superior = "SargentoMensajeriaYEnviosMasivos"
    mision = "Ejecución manual paso 2 para mensajeria_y_envios_masivos"
    eventos = ['tarea_manual_realizada']
    dependencias = []
