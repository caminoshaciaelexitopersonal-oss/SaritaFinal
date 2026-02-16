# backend/apps/sarita_agents/agents/soldado_template.py

import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class SoldierTemplate:
    """
    NIVEL 6 — SOLDADOS (Ejecución Manual Real)
    Ejecutan tareas específicas de registro, verificación, trazabilidad o monitoreo.
    """
    def __init__(self, sargento=None):
        self.sargento = sargento

    def execute(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Punto de entrada para la ejecución de la microtarea.
        """
        return self.handle_directive(task_data)

    def handle_directive(self, directive: Dict[str, Any]) -> Dict[str, Any]:
        """
        Integración sistémica Fase 4.1.
        """
        logger.info(f"SOLDADO ({self.__class__.__name__}): Ejecutando microtarea.")

        try:
            result = self.perform_action(directive)
            return {
                "status": "SUCCESS",
                "soldier": self.__class__.__name__,
                "result": result
            }
        except Exception as e:
            logger.error(f"SOLDADO ({self.__class__.__name__}): Fallo en ejecución -> {str(e)}")
            return {
                "status": "FAILED",
                "soldier": self.__class__.__name__,
                "error": str(e)
            }

    def perform_action(self, params: Dict[str, Any]):
        """Lógica concreta del soldado."""
        raise NotImplementedError("El método perform_action() debe ser implementado por cada Soldado.")
