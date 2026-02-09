# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import CapitanArchivisticoBase

logger = logging.getLogger(__name__)

class CapitanConservacionRetencion(CapitanArchivisticoBase):
    """
    CAPITÁN ARCHIVÍSTICO: conservacion
    Rol: Gobernar el ciclo de vida y permanencia.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CoronelArchivisticoGeneral
    Responsabilidad: Gobernar el ciclo de vida y permanencia.
    """
    nivel = "CAPITAN"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CoronelArchivisticoGeneral"
    responsabilidad_unica = "Gobernar el ciclo de vida y permanencia."

    def _get_tenientes(self) -> dict:
        """Declaración explícita de Tenientes subordinados."""
        return { "tenientepoliticaspurga": "TenientePoliticasPurga", "tenientepreservaciondigital": "TenientePreservacionDigital" }
