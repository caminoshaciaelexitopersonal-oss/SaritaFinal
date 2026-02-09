# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenienteTaxonomiaAutomatica(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenienteTaxonomiaAutomatica
    Rol: Coordinar la clasificación basada en IA.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanClasificacionMetadatos
    Responsabilidad: Coordinar la clasificación basada en IA.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanClasificacionMetadatos"
    responsabilidad_unica = "Coordinar la clasificación basada en IA."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentoetiquetadoia": "SargentoEtiquetadoIA" }
