# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenienteSelladoTiempo(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenienteSelladoTiempo
    Rol: Coordinar el timestamping blockchain.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanVersionadoTrazabilidad
    Responsabilidad: Coordinar el timestamping blockchain.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanVersionadoTrazabilidad"
    responsabilidad_unica = "Coordinar el timestamping blockchain."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentonotarizacionblockchain": "SargentoNotarizacionBlockchain" }
