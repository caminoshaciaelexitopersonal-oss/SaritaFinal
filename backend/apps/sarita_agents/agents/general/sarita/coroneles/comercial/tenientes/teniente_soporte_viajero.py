# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteSoporteViajero(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanSoporteViajero"
    mision = "Planificar tácticamente soporte_viajero"
    eventos = ['tactica_definida']
    dependencias = []
