# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoSeleccionAuditoria(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoSeleccionAuditoria
    Rol: Ejecutar la extracción aleatoria de documentos para revisión.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteMuestreoAleatorio
    Responsabilidad: Ejecutar la extracción aleatoria de documentos para revisión.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteMuestreoAleatorio"
    responsabilidad_unica = "Ejecutar la extracción aleatoria de documentos para revisión."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoSeleccionAuditoria_1", "SoldadoSeleccionAuditoria_2", "SoldadoSeleccionAuditoria_3", "SoldadoSeleccionAuditoria_4", "SoldadoSeleccionAuditoria_5" ]
