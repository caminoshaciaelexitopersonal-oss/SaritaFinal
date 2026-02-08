# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoGestionOperativaDeContenidosComerciales(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteGestionOperativaDeContenidosComerciales"
    mision = "Ejecutar acción atómica de gestion_operativa_de_contenidos_comerciales"
    eventos = ['accion_completada']
    dependencias = []
