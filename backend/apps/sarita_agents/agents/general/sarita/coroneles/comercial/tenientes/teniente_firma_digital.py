# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteFirmaDigital(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanFirmaDigital"
    mision = "Planificar tácticamente firma_digital"
    eventos = ['tactica_definida']
    dependencias = []
