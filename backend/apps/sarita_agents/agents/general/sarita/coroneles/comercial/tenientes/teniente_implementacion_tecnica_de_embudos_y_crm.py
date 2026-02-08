# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteImplementacionTecnicaDeEmbudosYCrm(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanImplementacionTecnicaDeEmbudosYCrm"
    mision = "Planificar tácticamente implementacion_tecnica_de_embudos_y_crm"
    eventos = ['tactica_definida']
    dependencias = []
