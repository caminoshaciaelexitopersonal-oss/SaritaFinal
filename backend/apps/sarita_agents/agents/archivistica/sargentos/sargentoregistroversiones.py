# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoRegistroVersiones(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoRegistroVersiones
    Rol: Ejecutar el incremento de versión y guardado de diffs.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteSeguimientoCambios
    Responsabilidad: Ejecutar el incremento de versión y guardado de diffs.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteSeguimientoCambios"
    responsabilidad_unica = "Ejecutar el incremento de versión y guardado de diffs."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoRegistroVersiones_1", "SoldadoRegistroVersiones_2", "SoldadoRegistroVersiones_3", "SoldadoRegistroVersiones_4", "SoldadoRegistroVersiones_5" ]
