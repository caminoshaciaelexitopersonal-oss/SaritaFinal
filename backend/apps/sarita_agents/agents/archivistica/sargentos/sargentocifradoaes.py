# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoCifradoAES(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoCifradoAES
    Rol: Ejecutar el cifrado de archivos en reposo.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteCifradoArchivos
    Responsabilidad: Ejecutar el cifrado de archivos en reposo.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteCifradoArchivos"
    responsabilidad_unica = "Ejecutar el cifrado de archivos en reposo."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoCifradoAES_1", "SoldadoCifradoAES_2", "SoldadoCifradoAES_3", "SoldadoCifradoAES_4", "SoldadoCifradoAES_5" ]
