# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoEscaneoFisico(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoEscaneoFisico
    Rol: Ejecutar el escaneo y conversión a PDF.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteDigitalizacionDirecta
    Responsabilidad: Ejecutar el escaneo y conversión a PDF.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteDigitalizacionDirecta"
    responsabilidad_unica = "Ejecutar el escaneo y conversión a PDF."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoEscaneoFisico_1", "SoldadoEscaneoFisico_2", "SoldadoEscaneoFisico_3", "SoldadoEscaneoFisico_4", "SoldadoEscaneoFisico_5" ]
