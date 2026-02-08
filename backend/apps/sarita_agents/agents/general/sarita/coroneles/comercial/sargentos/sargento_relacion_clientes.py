# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoRelacionClientes(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteRelacionClientes"
    mision = "Ejecutar acción atómica de relacion_clientes"
    eventos = ['accion_completada']
    dependencias = []
