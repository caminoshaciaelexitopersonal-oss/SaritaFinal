# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenientePreservacionDigital(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenientePreservacionDigital
    Rol: Coordinar la migración de formatos obsoletos.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanConservacionRetencion
    Responsabilidad: Coordinar la migración de formatos obsoletos.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanConservacionRetencion"
    responsabilidad_unica = "Coordinar la migración de formatos obsoletos."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentoconversionformato": "SargentoConversionFormato" }
