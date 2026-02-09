# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoGeneracionReporte(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoGeneracionReporte
    Rol: Ejecutar la compilación de evidencias en PDF.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteInformesCumplimiento
    Responsabilidad: Ejecutar la compilación de evidencias en PDF.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteInformesCumplimiento"
    responsabilidad_unica = "Ejecutar la compilación de evidencias en PDF."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoGeneracionReporte_1", "SoldadoGeneracionReporte_2", "SoldadoGeneracionReporte_3", "SoldadoGeneracionReporte_4", "SoldadoGeneracionReporte_5" ]
