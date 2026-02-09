# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoMarcadoEliminacion(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoMarcadoEliminacion
    Rol: Ejecutar el cambio de estado a 'Pendiente de Destrucción'.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenientePoliticasPurga
    Responsabilidad: Ejecutar el cambio de estado a 'Pendiente de Destrucción'.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenientePoliticasPurga"
    responsabilidad_unica = "Ejecutar el cambio de estado a 'Pendiente de Destrucción'."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoMarcadoEliminacion_1", "SoldadoMarcadoEliminacion_2", "SoldadoMarcadoEliminacion_3", "SoldadoMarcadoEliminacion_4", "SoldadoMarcadoEliminacion_5" ]
