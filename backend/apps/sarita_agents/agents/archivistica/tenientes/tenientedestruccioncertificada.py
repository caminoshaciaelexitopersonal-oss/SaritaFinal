# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import TenienteArchivisticoBase

logger = logging.getLogger(__name__)

class TenienteDestruccionCertificada(TenienteArchivisticoBase):
    """
    TENIENTE ARCHIVÍSTICO: TenienteDestruccionCertificada
    Rol: Coordinar el borrado seguro de datos.
    Dominio: GESTION_ARCHIVISTICA
    Superior: CapitanEliminacionGobernada
    Responsabilidad: Coordinar el borrado seguro de datos.
    """
    nivel = "TENIENTE"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "CapitanEliminacionGobernada"
    responsabilidad_unica = "Coordinar el borrado seguro de datos."

    def _get_sargentos(self) -> dict:
        """Declaración de Sargentos subordinados."""
        return { "sargentoborradoseguro": "SargentoBorradoSeguro" }
