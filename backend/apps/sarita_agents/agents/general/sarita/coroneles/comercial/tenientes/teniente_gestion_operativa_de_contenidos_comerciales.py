# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import TenienteComercialBase

logger = logging.getLogger(__name__)

class TenienteGestionOperativaDeContenidosComerciales(TenienteComercialBase):
    nivel = "TENIENTE"
    dominio = "GESTION_COMERCIAL"
    superior = "CapitanGestionOperativaDeContenidosComerciales"
    mision = "Planificar tácticamente gestion_operativa_de_contenidos_comerciales"
    eventos = ['tactica_definida']
    dependencias = []
