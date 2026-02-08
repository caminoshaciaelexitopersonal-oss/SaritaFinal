# backend/apps/sarita_agents/agents/sargento_template.py

import logging
from apps.sarita_agents.models import RegistroDeEjecucion

logger = logging.getLogger(__name__)

class SargentoTemplate:
    """
    Plantilla base para todos los Sargentos.
    Ejecutan acciones mínimas indivisibles. No deciden, no interpretan.
    """
    def __init__(self, teniente):
        self.teniente = teniente

    def execute(self, action_data: dict) -> dict:
        """
        Punto de entrada para la ejecución atómica.
        Toda ejecución queda registrada.
        """
        sargento_name = self.__class__.__name__
        logger.info(f"SARGENTO ({sargento_name}): Ejecutando acción atómica.")

        try:
            result = self.perform_atomic_action(action_data)
            logger.info(f"SARGENTO ({sargento_name}): Acción completada.")
            return {"status": "SUCCESS", "data": result}
        except Exception as e:
            logger.error(f"SARGENTO ({sargento_name}): Error en ejecución atómica -> {str(e)}")
            return {"status": "ERROR", "message": str(e)}

    def perform_atomic_action(self, action_data: dict):
        raise NotImplementedError("El método perform_atomic_action() debe ser implementado.")
