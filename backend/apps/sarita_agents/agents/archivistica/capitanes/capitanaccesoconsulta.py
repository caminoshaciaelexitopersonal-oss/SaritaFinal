# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import CapitanArchivisticoBase

logger = logging.getLogger(__name__)

class CapitanAccesoConsulta(CapitanArchivisticoBase):
    """
    CAPITÁN ARCHIVÍSTICO: acceso
    Rol: Gobernar los permisos y visualización de documentos.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CoronelArchivisticoGeneral
    Responsabilidad: Gobernar los permisos y visualización de documentos.
    """
    nivel = "CAPITAN"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CoronelArchivisticoGeneral"
    responsabilidad_unica = "Gobernar los permisos y visualización de documentos."

    def _get_tenientes(self) -> dict:
        """Declaración explícita de Tenientes subordinados."""
        return { "tenientecontrolpermisos": "TenienteControlPermisos", "tenientemotorbusqueda": "TenienteMotorBusqueda" }
