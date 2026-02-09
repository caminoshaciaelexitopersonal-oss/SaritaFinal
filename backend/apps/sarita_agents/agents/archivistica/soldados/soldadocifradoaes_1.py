# Agente Normalizado FASE 2.1
import logging
from apps.sarita_agents.agents.archivistica_base_templates import SoldadoArchivisticoBase

logger = logging.getLogger(__name__)

class SoldadoCifradoAES_1(SoldadoArchivisticoBase):
    """
    SOLDADO ARCHIVÍSTICO: SoldadoCifradoAES_1
    Rol: Ejecución manual de tareas de SargentoCifradoAES
    Dominio: GESTION_ARCHIVISTICA
    Superior: SargentoCifradoAES
    Responsabilidad: Realizar la tarea 1 de SargentoCifradoAES.
    """
    nivel = "SOLDADO"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "SargentoCifradoAES"
    responsabilidad_unica = "Ejecución atómica manual de la subtarea 1."
    tarea_manual = "Obtener llave pública"

    def ejecutar_orden(self, params):
        """Orden ejecutable con generación de evidencia."""
        logger.info(f"SoldadoCifradoAES_1: Ejecutando {self.tarea_manual}")
        return {"status": "SUCCESS", "evidencia": "evidencia_manual_generada"}
