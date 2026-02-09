# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenientePoliticasPurga(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenientePoliticasPurga
    Rol: Coordinar el cumplimiento de tiempos legales.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanConservacionRetencion
    Responsabilidad: Coordinar el cumplimiento de tiempos legales.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanConservacionRetencion"
    responsabilidad_unica = "Coordinar el cumplimiento de tiempos legales."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentomarcadoeliminacion": "SargentoMarcadoEliminacion" }
