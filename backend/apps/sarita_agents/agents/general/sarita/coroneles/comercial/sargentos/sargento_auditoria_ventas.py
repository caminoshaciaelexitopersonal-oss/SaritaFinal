# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoAuditoriaVentas(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteAuditoriaVentas"
    mision = "Ejecutar acción atómica de auditoria_ventas"
    eventos = ['accion_completada']
    dependencias = []
