# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SoldadoComercialBase

logger = logging.getLogger(__name__)

class SoldadoGestionComercialGeneral2(SoldadoComercialBase):
    nivel = "SOLDADO"
    dominio = "GESTION_COMERCIAL"
    superior = "SargentoGestionComercialGeneral"
    mision = "Ejecución manual paso 2 para gestion_comercial_general"
    eventos = ['tarea_manual_realizada']
    dependencias = []
