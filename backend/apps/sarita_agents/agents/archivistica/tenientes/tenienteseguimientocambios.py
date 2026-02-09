# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenienteSeguimientoCambios(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenienteSeguimientoCambios
    Rol: Coordinar el historial de versiones.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanVersionadoTrazabilidad
    Responsabilidad: Coordinar el historial de versiones.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanVersionadoTrazabilidad"
    responsabilidad_unica = "Coordinar el historial de versiones."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentoregistroversiones": "SargentoRegistroVersiones" }
