# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import CapitanArchivisticoBase

logger = logging.getLogger(__name__)

class CapitanCustodiaAlmacenamiento(CapitanArchivisticoBase):
    """
    CAPITÁN ARCHIVÍSTICO: custodia
    Rol: Gobernar el almacenamiento seguro y cifrado.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CoronelArchivisticoGeneral
    Responsabilidad: Gobernar el almacenamiento seguro y cifrado.
    """
    nivel = "CAPITAN"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CoronelArchivisticoGeneral"
    responsabilidad_unica = "Gobernar el almacenamiento seguro y cifrado."

    def _get_tenientes(self) -> dict:
        """Declaración explícita de Tenientes subordinados."""
        return { "tenientecifradoarchivos": "TenienteCifradoArchivos", "tenientegestionboveda": "TenienteGestionBoveda" }
