# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SoldadoComercialBase

logger = logging.getLogger(__name__)

class SoldadoFirmaDigital4(SoldadoComercialBase):
    nivel = "SOLDADO"
    dominio = "GESTION_COMERCIAL"
    superior = "SargentoFirmaDigital"
    mision = "Ejecución manual paso 4 para firma_digital"
    eventos = ['tarea_manual_realizada']
    dependencias = []
