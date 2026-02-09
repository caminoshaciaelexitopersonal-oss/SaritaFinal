# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenienteControlPermisos(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenienteControlPermisos
    Rol: Coordinar la ACL de acceso por roles.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanAccesoConsulta
    Responsabilidad: Coordinar la ACL de acceso por roles.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanAccesoConsulta"
    responsabilidad_unica = "Coordinar la ACL de acceso por roles."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentovalidacionacl": "SargentoValidacionACL" }
