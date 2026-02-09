# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoCertificacionDestruccion(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoCertificacionDestruccion
    Rol: Ejecutar la firma digital del acta de eliminación.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteAuditoriaEliminacion
    Responsabilidad: Ejecutar la firma digital del acta de eliminación.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteAuditoriaEliminacion"
    responsabilidad_unica = "Ejecutar la firma digital del acta de eliminación."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoCertificacionDestruccion_1", "SoldadoCertificacionDestruccion_2", "SoldadoCertificacionDestruccion_3", "SoldadoCertificacionDestruccion_4", "SoldadoCertificacionDestruccion_5" ]
