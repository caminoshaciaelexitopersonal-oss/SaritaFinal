# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import CapitanComercialBase

logger = logging.getLogger(__name__)

class CapitanImplementacionTecnicaDeEmbudosYCrm(CapitanComercialBase):
    nivel = "CAPITAN"
    dominio = "GESTION_COMERCIAL"
    superior = "CoronelComercialGeneral"
    mision = "Gobernar el dominio comercial de implementacion_tecnica_de_embudos_y_crm"
    eventos = ['mision_planificada']
    dependencias = []
