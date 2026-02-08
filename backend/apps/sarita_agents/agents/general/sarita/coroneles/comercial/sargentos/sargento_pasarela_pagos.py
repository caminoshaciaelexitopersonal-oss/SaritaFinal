# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoPasarelaPagos(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenientePasarelaPagos"
    mision = "Ejecutar acción atómica de pasarela_pagos"
    eventos = ['accion_completada']
    dependencias = []
