# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import CapitanArchivisticoBase

logger = logging.getLogger(__name__)

class CapitanEliminacionGobernada(CapitanArchivisticoBase):
    """
    CAPITÁN ARCHIVÍSTICO: eliminacion
    Rol: Gobernar la destrucción certificada y auditada.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CoronelArchivisticoGeneral
    Responsabilidad: Gobernar la destrucción certificada y auditada.
    """
    nivel = "CAPITAN"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CoronelArchivisticoGeneral"
    responsabilidad_unica = "Gobernar la destrucción certificada y auditada."

    def _get_tenientes(self) -> dict:
        """Declaración explícita de Tenientes subordinados."""
        return { "tenientedestruccioncertificada": "TenienteDestruccionCertificada", "tenienteauditoriaeliminacion": "TenienteAuditoriaEliminacion" }
