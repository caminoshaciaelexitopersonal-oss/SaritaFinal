# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SoldadoComercialBase

logger = logging.getLogger(__name__)

class SoldadoCotizacionesDinamicas2(SoldadoComercialBase):
    nivel = "SOLDADO"
    dominio = "GESTION_COMERCIAL"
    superior = "SargentoCotizacionesDinamicas"
    mision = "Ejecución manual paso 2 para cotizaciones_dinamicas"
    eventos = ['tarea_manual_realizada']
    dependencias = []
