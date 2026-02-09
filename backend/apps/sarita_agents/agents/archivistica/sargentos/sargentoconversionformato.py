# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoConversionFormato(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoConversionFormato
    Rol: Ejecutar la transcodificación a formatos de archivo a largo plazo.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenientePreservacionDigital
    Responsabilidad: Ejecutar la transcodificación a formatos de archivo a largo plazo.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenientePreservacionDigital"
    responsabilidad_unica = "Ejecutar la transcodificación a formatos de archivo a largo plazo."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoConversionFormato_1", "SoldadoConversionFormato_2", "SoldadoConversionFormato_3", "SoldadoConversionFormato_4", "SoldadoConversionFormato_5" ]
