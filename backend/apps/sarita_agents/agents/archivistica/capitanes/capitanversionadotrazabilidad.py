# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import CapitanArchivisticoBase

logger = logging.getLogger(__name__)

class CapitanVersionadoTrazabilidad(CapitanArchivisticoBase):
    """
    CAPITÁN ARCHIVÍSTICO: versionado
    Rol: Gobernar el historial de cambios y hashes.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CoronelArchivisticoGeneral
    Responsabilidad: Gobernar el historial de cambios y hashes.
    """
    nivel = "CAPITAN"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CoronelArchivisticoGeneral"
    responsabilidad_unica = "Gobernar el historial de cambios y hashes."

    def _get_tenientes(self) -> dict:
        """Declaración explícita de Tenientes subordinados."""
        return { "tenienteseguimientocambios": "TenienteSeguimientoCambios", "tenienteselladotiempo": "TenienteSelladoTiempo" }
