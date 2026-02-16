from apps.sarita_agents.agents.soldado_template import SoldierTemplate
import logging

logger = logging.getLogger(__name__)

class SoldadoRiesgos(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO RIESGOS: Evaluando factor de riesgo step {params.get('step')}")
        return {"detail": "Riesgo evaluado"}

class SoldadoIncidentes(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO INCIDENTES: Registrando evidencia step {params.get('step')}")
        return {"detail": "Incidente registrado"}

class SoldadoCapacitacion(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO CAPACITACION: Verificando asistencia step {params.get('step')}")
        return {"detail": "Capacitación verificada"}

class SoldadoInspecciones(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO INSPECCIONES: Ejecutando checklist step {params.get('step')}")
        return {"detail": "Inspección ejecutada"}

class SoldadoIndicadores(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO INDICADORES: Procesando datos step {params.get('step')}")
        return {"detail": "Indicador calculado"}
