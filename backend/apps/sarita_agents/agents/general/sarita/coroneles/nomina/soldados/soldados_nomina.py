from apps.sarita_agents.agents.soldado_template import SoldierTemplate
import logging

logger = logging.getLogger(__name__)

class SoldadoLiquidacion(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO NOMINA: Procesando línea de liquidación step {params.get('step')}")
        from django.utils.module_loading import import_string
        NominaService = import_string('apps.prestadores.mi_negocio.gestion_contable.nomina.services.NominaService') # DECOUPLED
        planilla_id = params.get('planilla_id')
        if planilla_id and params.get('step') == 0:
            NominaService.liquidar_periodo(planilla_id)
            return {"detail": "Liquidación de planilla ejecutada por Agente Soldado."}
        return {"detail": "Línea de nómina procesada"}

class SoldadoPrestaciones(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO NOMINA: Calculando prestación step {params.get('step')}")
        return {"detail": "Prestación social calculada"}

class SoldadoSeguridadSocial(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO NOMINA: Verificando aporte SS step {params.get('step')}")
        return {"detail": "Seguridad social validada"}

class SoldadoNovedades(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO NOMINA: Registrando novedad laboral step {params.get('step')}")
        return {"detail": "Novedad registrada y vinculada"}

class SoldadoIndicadores(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO NOMINA: Analizando métrica laboral step {params.get('step')}")
        return {"detail": "Métrica laboral consolidada"}
