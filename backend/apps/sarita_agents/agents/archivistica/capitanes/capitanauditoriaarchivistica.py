# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import CapitanArchivisticoBase

logger = logging.getLogger(__name__)

class CapitanAuditoriaArchivistica(CapitanArchivisticoBase):
    """
    CAPITÁN ARCHIVÍSTICO: auditoria
    Rol: Gobernar la verificación de integridad sistémica.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CoronelArchivisticoGeneral
    Responsabilidad: Gobernar la verificación de integridad sistémica.
    """
    nivel = "CAPITAN"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CoronelArchivisticoGeneral"
    responsabilidad_unica = "Gobernar la verificación de integridad sistémica."

    def _get_tenientes(self) -> dict:
        """Declaración explícita de Tenientes subordinados."""
        return { "tenientemuestreoaleatorio": "TenienteMuestreoAleatorio", "tenienteinformescumplimiento": "TenienteInformesCumplimiento" }
