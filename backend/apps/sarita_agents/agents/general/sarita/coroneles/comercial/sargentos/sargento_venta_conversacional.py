# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoVentaConversacional(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteVentaConversacional"
    mision = "Ejecutar acción atómica de venta_conversacional"
    eventos = ['accion_completada']
    dependencias = []
