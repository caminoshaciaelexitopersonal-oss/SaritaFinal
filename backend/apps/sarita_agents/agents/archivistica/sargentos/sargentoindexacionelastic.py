# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoIndexacionElastic(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoIndexacionElastic
    Rol: Ejecutar el envío de metadatos al motor de búsqueda.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteMotorBusqueda
    Responsabilidad: Ejecutar el envío de metadatos al motor de búsqueda.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteMotorBusqueda"
    responsabilidad_unica = "Ejecutar el envío de metadatos al motor de búsqueda."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoIndexacionElastic_1", "SoldadoIndexacionElastic_2", "SoldadoIndexacionElastic_3", "SoldadoIndexacionElastic_4", "SoldadoIndexacionElastic_5" ]
