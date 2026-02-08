# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SoldadoComercialBase

logger = logging.getLogger(__name__)

class SoldadoConversion3(SoldadoComercialBase):
    nivel = "SOLDADO"
    dominio = "GESTION_COMERCIAL"
    superior = "SargentoConversion"
    mision = "Ejecución manual paso 3 para conversion"
    eventos = ['tarea_manual_realizada']
    dependencias = []
