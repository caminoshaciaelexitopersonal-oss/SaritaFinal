# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenienteAuditoriaEliminacion(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenienteAuditoriaEliminacion
    Rol: Coordinar la generación de certificados de destrucción.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanEliminacionGobernada
    Responsabilidad: Coordinar la generación de certificados de destrucción.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanEliminacionGobernada"
    responsabilidad_unica = "Coordinar la generación de certificados de destrucción."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentocertificaciondestruccion": "SargentoCertificacionDestruccion" }
