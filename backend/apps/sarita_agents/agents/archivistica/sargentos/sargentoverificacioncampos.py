# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoVerificacionCampos(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoVerificacionCampos
    Rol: Ejecutar la validación de esquemas JSON de metadatos.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteValidacionMetadatos
    Responsabilidad: Ejecutar la validación de esquemas JSON de metadatos.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteValidacionMetadatos"
    responsabilidad_unica = "Ejecutar la validación de esquemas JSON de metadatos."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoVerificacionCampos_1", "SoldadoVerificacionCampos_2", "SoldadoVerificacionCampos_3", "SoldadoVerificacionCampos_4", "SoldadoVerificacionCampos_5" ]
