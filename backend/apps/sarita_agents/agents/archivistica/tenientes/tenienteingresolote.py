# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenienteIngresoLote(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenienteIngresoLote
    Rol: Coordinar la carga masiva de archivos externos.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanCapturaDocumental
    Responsabilidad: Coordinar la carga masiva de archivos externos.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanCapturaDocumental"
    responsabilidad_unica = "Coordinar la carga masiva de archivos externos."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentoprocesamientozip": "SargentoProcesamientoZip" }
