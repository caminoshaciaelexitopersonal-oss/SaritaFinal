# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SoldadoComercialBase

logger = logging.getLogger(__name__)

class SoldadoPasarelaPagos4(SoldadoComercialBase):
    nivel = "SOLDADO"
    dominio = "GESTION_COMERCIAL"
    superior = "SargentoPasarelaPagos"
    mision = "Ejecución manual paso 4 para pasarela_pagos"
    eventos = ['tarea_manual_realizada']
    dependencias = []
