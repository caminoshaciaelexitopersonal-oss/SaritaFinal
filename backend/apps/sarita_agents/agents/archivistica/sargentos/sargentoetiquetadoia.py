# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoEtiquetadoIA(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoEtiquetadoIA
    Rol: Ejecutar el motor de reconocimiento de entidades.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteTaxonomiaAutomatica
    Responsabilidad: Ejecutar el motor de reconocimiento de entidades.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteTaxonomiaAutomatica"
    responsabilidad_unica = "Ejecutar el motor de reconocimiento de entidades."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoEtiquetadoIA_1", "SoldadoEtiquetadoIA_2", "SoldadoEtiquetadoIA_3", "SoldadoEtiquetadoIA_4", "SoldadoEtiquetadoIA_5" ]
