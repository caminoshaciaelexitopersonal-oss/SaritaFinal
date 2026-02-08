# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SoldadoComercialBase

logger = logging.getLogger(__name__)

class SoldadoComercialTransporte2(SoldadoComercialBase):
    nivel = "SOLDADO"
    dominio = "GESTION_COMERCIAL"
    superior = "SargentoComercialTransporte"
    mision = "Ejecución manual paso 2 para comercial_transporte"
    eventos = ['tarea_manual_realizada']
    dependencias = []
