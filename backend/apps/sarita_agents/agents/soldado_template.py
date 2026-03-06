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
        Integración sistémica Fase 4.1 (Observabilidad).
        """
        from apps.common.observability.middleware import get_correlation_id

        logger.info(
            f"SOLDADO ({self.__class__.__name__}): Ejecutando microtarea.",
            extra={"extra_fields": {"correlation_id": get_correlation_id(), "agent_level": "N6"}}
        )

        try:
            result = self.perform_action(directive)

            logger.info(
                f"SOLDADO ({self.__class__.__name__}): Microtarea completada.",
                extra={"extra_fields": {"status": "SUCCESS", "correlation_id": get_correlation_id()}}
            )

            return {
                "status": "SUCCESS",
                "soldier": self.__class__.__name__,
                "result": result,
                "correlation_id": get_correlation_id()
            }
        except Exception as e:
            logger.error(
                f"SOLDADO ({self.__class__.__name__}): Fallo en ejecución -> {str(e)}",
                extra={"extra_fields": {"status": "FAILED", "correlation_id": get_correlation_id()}}
            )
            return {
                "status": "FAILED",
                "soldier": self.__class__.__name__,
                "error": str(e),
                "correlation_id": get_correlation_id()
            }

    def perform_action(self, params: Dict[str, Any]):
        """Lógica concreta del soldado."""
        raise NotImplementedError("El método perform_action() debe ser implementado por cada Soldado.")
