# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenienteGestionBoveda(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenienteGestionBoveda
    Rol: Coordinar la replicación en bóvedas seguras.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanCustodiaAlmacenamiento
    Responsabilidad: Coordinar la replicación en bóvedas seguras.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanCustodiaAlmacenamiento"
    responsabilidad_unica = "Coordinar la replicación en bóvedas seguras."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentoreplicacioncloud": "SargentoReplicacionCloud" }
