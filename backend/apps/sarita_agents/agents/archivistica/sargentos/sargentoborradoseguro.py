# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SargentoArchivisticoBase

logger = logging.getLogger(__name__)

class SargentoBorradoSeguro(SargentoArchivisticoBase):
    """
    SARGENTO ARCHIVÍSTICO: SargentoBorradoSeguro
    Rol: Ejecutar el borrado físico de 7 pasadas.
    Dominio: GESTION_ARCHIVISTICA
    Superior: TenienteDestruccionCertificada
    Responsabilidad: Ejecutar el borrado físico de 7 pasadas.
    """
    nivel = "SARGENTO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "TenienteDestruccionCertificada"
    responsabilidad_unica = "Ejecutar el borrado físico de 7 pasadas."

    def _get_soldados(self) -> list:
        """Declaración de Soldados subordinados."""
        return [ "SoldadoBorradoSeguro_1", "SoldadoBorradoSeguro_2", "SoldadoBorradoSeguro_3", "SoldadoBorradoSeguro_4", "SoldadoBorradoSeguro_5" ]
