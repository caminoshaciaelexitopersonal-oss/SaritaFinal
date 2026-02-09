# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenienteMotorBusqueda(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenienteMotorBusqueda
    Rol: Coordinar la indexación para recuperación rápida.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanAccesoConsulta
    Responsabilidad: Coordinar la indexación para recuperación rápida.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanAccesoConsulta"
    responsabilidad_unica = "Coordinar la indexación para recuperación rápida."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentoindexacionelastic": "SargentoIndexacionElastic" }
