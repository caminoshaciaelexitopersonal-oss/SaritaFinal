# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenienteMuestreoAleatorio(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenienteMuestreoAleatorio
    Rol: Coordinar auditorías sorpresivas de integridad.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanAuditoriaArchivistica
    Responsabilidad: Coordinar auditorías sorpresivas de integridad.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanAuditoriaArchivistica"
    responsabilidad_unica = "Coordinar auditorías sorpresivas de integridad."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentoseleccionauditoria": "SargentoSeleccionAuditoria" }
