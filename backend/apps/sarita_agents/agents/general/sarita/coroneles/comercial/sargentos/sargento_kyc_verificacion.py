# Agente Normalizado FASE 1.1
import logging
from apps.sarita_agents.agents.comercial_base_templates import SargentoComercialBase

logger = logging.getLogger(__name__)

class SargentoKycVerificacion(SargentoComercialBase):
    nivel = "SARGENTO"
    dominio = "GESTION_COMERCIAL"
    superior = "TenienteKycVerificacion"
    mision = "Ejecutar acción atómica de kyc_verificacion"
    eventos = ['accion_completada']
    dependencias = []
