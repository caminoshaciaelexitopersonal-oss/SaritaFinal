# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenienteInformesCumplimiento(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenienteInformesCumplimiento
    Rol: Coordinar reportes de cumplimiento normativo.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanAuditoriaArchivistica
    Responsabilidad: Coordinar reportes de cumplimiento normativo.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanAuditoriaArchivistica"
    responsabilidad_unica = "Coordinar reportes de cumplimiento normativo."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentogeneracionreporte": "SargentoGeneracionReporte" }
