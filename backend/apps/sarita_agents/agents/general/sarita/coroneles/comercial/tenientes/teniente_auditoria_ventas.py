# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteAuditoriaVentas(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanAuditoriaVentas"
    mision = "Planificar tácticamente auditoria_ventas"
    eventos = ['tactica_definida']
    dependencias = []
