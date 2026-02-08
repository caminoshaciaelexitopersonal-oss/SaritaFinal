# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteAlianzasComerciales(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanAlianzasComerciales"
    mision = "Planificar tácticamente alianzas_comerciales"
    eventos = ['tactica_definida']
    dependencias = []
