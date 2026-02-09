# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import CapitanArchivisticoBase

logger = logging.getLogger(__name__)

class CapitanCapturaDocumental(CapitanArchivisticoBase):
    """
    CAPITÁN ARCHIVÍSTICO: captura
    Rol: Gobernar el ingreso y digitalización de documentos.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CoronelArchivisticoGeneral
    Responsabilidad: Gobernar el ingreso y digitalización de documentos.
    """
    nivel = "CAPITAN"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CoronelArchivisticoGeneral"
    responsabilidad_unica = "Gobernar el ingreso y digitalización de documentos."

    def _get_tenientes(self) -> dict:
        """Declaración explícita de Tenientes subordinados."""
        return { "tenientedigitalizaciondirecta": "TenienteDigitalizacionDirecta", "tenienteingresolote": "TenienteIngresoLote" }
