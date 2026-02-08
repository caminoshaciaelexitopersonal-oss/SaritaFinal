# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteRelacionClientes(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanRelacionClientes"
    mision = "Planificar tácticamente relacion_clientes"
    eventos = ['tactica_definida']
    dependencias = []
