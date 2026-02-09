# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import CapitanArchivisticoBase

logger = logging.getLogger(__name__)

class CapitanClasificacionMetadatos(CapitanArchivisticoBase):
    """
    CAPITÁN ARCHIVÍSTICO: clasificacion
    Rol: Gobernar la taxonomía y asignación de metadatos.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CoronelArchivisticoGeneral
    Responsabilidad: Gobernar la taxonomía y asignación de metadatos.
    """
    nivel = "CAPITAN"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CoronelArchivisticoGeneral"
    responsabilidad_unica = "Gobernar la taxonomía y asignación de metadatos."

    def _get_tenientes(self) -> dict:
        """Declaración explícita de Tenientes subordinados."""
        return { "tenientetaxonomiaautomatica": "TenienteTaxonomiaAutomatica", "tenientevalidacionmetadatos": "TenienteValidacionMetadatos" }
