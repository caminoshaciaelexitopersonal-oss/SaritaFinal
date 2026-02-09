# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoReplicacionCloud(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoReplicacionCloud
    Rol: Ejecutar la subida a buckets de alta disponibilidad.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteGestionBoveda
    Responsabilidad: Ejecutar la subida a buckets de alta disponibilidad.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteGestionBoveda"
    responsabilidad_unica = "Ejecutar la subida a buckets de alta disponibilidad."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoReplicacionCloud_1", "SoldadoReplicacionCloud_2", "SoldadoReplicacionCloud_3", "SoldadoReplicacionCloud_4", "SoldadoReplicacionCloud_5" ]
