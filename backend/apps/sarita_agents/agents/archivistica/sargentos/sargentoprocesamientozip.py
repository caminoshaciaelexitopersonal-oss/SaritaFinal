# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoProcesamientoZip(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoProcesamientoZip
    Rol: Ejecutar la descompresión y validación de integridad de lotes.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteIngresoLote
    Responsabilidad: Ejecutar la descompresión y validación de integridad de lotes.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteIngresoLote"
    responsabilidad_unica = "Ejecutar la descompresión y validación de integridad de lotes."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoProcesamientoZip_1", "SoldadoProcesamientoZip_2", "SoldadoProcesamientoZip_3", "SoldadoProcesamientoZip_4", "SoldadoProcesamientoZip_5" ]
