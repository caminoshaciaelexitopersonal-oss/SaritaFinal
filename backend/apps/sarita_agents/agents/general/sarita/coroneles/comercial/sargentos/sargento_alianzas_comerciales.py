# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoAlianzasComerciales(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteAlianzasComerciales"
    mision = "Ejecutar acción atómica de alianzas_comerciales"
    eventos = ['accion_completada']
    dependencias = []
