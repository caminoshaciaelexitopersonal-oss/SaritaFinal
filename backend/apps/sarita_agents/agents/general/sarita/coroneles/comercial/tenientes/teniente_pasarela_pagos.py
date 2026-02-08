# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenientePasarelaPagos(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanPasarelaPagos"
    mision = "Planificar tácticamente pasarela_pagos"
    eventos = ['tactica_definida']
    dependencias = []
