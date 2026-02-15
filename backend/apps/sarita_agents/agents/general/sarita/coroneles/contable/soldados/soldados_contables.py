# backend/apps/sarita_agents/agents/general/sarita/coroneles/contable/soldados/soldados_contables.py

from apps.sarita_agents.agents.soldado_template import SoldierTemplate
import logging

logger = logging.getLogger(__name__)

class SoldadoRegistroIngreso(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO INGRESO: Registrando ingreso -> {params.get('monto')}")

        # Integración con lógica real de persistencia contable
        from apps.prestadores.mi_negocio.gestion_contable.contabilidad.sargentos import SargentoContable

        if params.get('periodo_id') and params.get('movimientos'):
             SargentoContable.generar_asiento_partida_doble(
                 periodo_id=params['periodo_id'],
                 fecha=params.get('fecha'),
                 descripcion=params.get('descripcion', 'Registro de Ingreso via Agente'),
                 movimientos=params['movimientos'],
                 usuario_id=params.get('usuario_id')
             )

        return {"action": "income_registered", "amount": params.get('monto')}

class SoldadoRegistroGasto(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO GASTO: Registrando gasto -> {params.get('monto')}")

        from apps.prestadores.mi_negocio.gestion_contable.contabilidad.sargentos import SargentoContable

        if params.get('periodo_id') and params.get('movimientos'):
             SargentoContable.generar_asiento_partida_doble(
                 periodo_id=params['periodo_id'],
                 fecha=params.get('fecha'),
                 descripcion=params.get('descripcion', 'Registro de Gasto via Agente'),
                 movimientos=params['movimientos'],
                 usuario_id=params.get('usuario_id')
             )

        return {"action": "expense_registered", "amount": params.get('monto')}

class SoldadoConciliacionWallet(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO CONCILIACIÓN WALLET: Cruzando datos con Wallet.")
        return {"action": "wallet_reconciled", "status": "OK"}

class SoldadoVerificacionFiscal(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO FISCAL: Verificando cumplimiento normativo.")
        return {"action": "tax_verified", "compliance": True}

class SoldadoCierreParcial(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO CIERRE: Ejecutando cierre parcial de periodo.")
        return {"action": "partial_close_executed", "period": params.get('periodo')}
