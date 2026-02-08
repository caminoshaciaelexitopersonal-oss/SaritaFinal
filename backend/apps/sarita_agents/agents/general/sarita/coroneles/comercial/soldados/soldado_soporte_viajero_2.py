# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SoldadoComercialBase

logger = logging.getLogger(__name__)

class SoldadoSoporteViajero2(SoldadoComercialBase):
    nivel = "SOLDADO"
    dominio = "GESTION_COMERCIAL"
    superior = "SargentoSoporteViajero"
    mision = "Ejecución manual paso 2 para soporte_viajero"
    eventos = ['tarea_manual_realizada']
    dependencias = []
