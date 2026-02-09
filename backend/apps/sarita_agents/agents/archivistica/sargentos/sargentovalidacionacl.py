# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoValidacionACL(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoValidacionACL
    Rol: Ejecutar la verificación de tokens de acceso.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteControlPermisos
    Responsabilidad: Ejecutar la verificación de tokens de acceso.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteControlPermisos"
    responsabilidad_unica = "Ejecutar la verificación de tokens de acceso."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoValidacionACL_1", "SoldadoValidacionACL_2", "SoldadoValidacionACL_3", "SoldadoValidacionACL_4", "SoldadoValidacionACL_5" ]
