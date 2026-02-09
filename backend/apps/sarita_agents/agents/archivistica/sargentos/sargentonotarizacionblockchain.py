# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoNotarizacionBlockchain(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoNotarizacionBlockchain
    Rol: Ejecutar la transacción de hash en la red Polygon.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteSelladoTiempo
    Responsabilidad: Ejecutar la transacción de hash en la red Polygon.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteSelladoTiempo"
    responsabilidad_unica = "Ejecutar la transacción de hash en la red Polygon."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoNotarizacionBlockchain_1", "SoldadoNotarizacionBlockchain_2", "SoldadoNotarizacionBlockchain_3", "SoldadoNotarizacionBlockchain_4", "SoldadoNotarizacionBlockchain_5" ]
