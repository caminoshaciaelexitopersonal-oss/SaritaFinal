# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenienteDigitalizacionDirecta(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenienteDigitalizacionDirecta
    Rol: Coordinar la digitalización física de documentos.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanCapturaDocumental
    Responsabilidad: Coordinar la digitalización física de documentos.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanCapturaDocumental"
    responsabilidad_unica = "Coordinar la digitalización física de documentos."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentoescaneofisico": "SargentoEscaneoFisico" }
