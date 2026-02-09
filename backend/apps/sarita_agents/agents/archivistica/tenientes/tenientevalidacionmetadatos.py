# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenienteValidacionMetadatos(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenienteValidacionMetadatos
    Rol: Coordinar la verificación de campos obligatorios.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanClasificacionMetadatos
    Responsabilidad: Coordinar la verificación de campos obligatorios.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanClasificacionMetadatos"
    responsabilidad_unica = "Coordinar la verificación de campos obligatorios."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentoverificacioncampos": "SargentoVerificacionCampos" }
