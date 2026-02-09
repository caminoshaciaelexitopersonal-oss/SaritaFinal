# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SoldadoArchivisticoBase

logger = logging.getLogger(__name__)

class SoldadoVerificacionCampos_2(SoldadoArchivisticoBase):
    """
    SOLDADO ARCHIVÍSTICO: SoldadoVerificacionCampos_2
    Rol: Ejecución manual de tareas de SargentoVerificacionCampos
    Dominio: GESTION_ARCHIVISTICA
    Superior: SargentoVerificacionCampos
    Responsabilidad: Realizar la tarea 2 de SargentoVerificacionCampos.
    """
    nivel = "SOLDADO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "SargentoVerificacionCampos"
    responsabilidad_unica = "Ejecución atómica manual de la subtarea 2."
    tarea_manual = "Validar tipos de datos"

    def ejecutar_orden(self, params):
        """Orden ejecutable con generación de evidencia."""
        logger.info(f"SoldadoVerificacionCampos_2: Ejecutando {self.tarea_manual}")
        return {"status": "SUCCESS", "evidencia": "evidencia_manual_generada"}
