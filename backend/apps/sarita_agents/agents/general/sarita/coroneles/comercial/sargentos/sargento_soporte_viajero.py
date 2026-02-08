# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoSoporteViajero(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteSoporteViajero"
    mision = "Ejecutar acción atómica de soporte_viajero"
    eventos = ['accion_completada']
    dependencias = []
