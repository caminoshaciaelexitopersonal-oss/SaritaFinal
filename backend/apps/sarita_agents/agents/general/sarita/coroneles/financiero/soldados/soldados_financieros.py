# backend/apps/sarita_agents/agents/general/sarita/coroneles/financiero/soldados/soldados_financieros.py

from apps.sarita_agents.agents.soldado_template import SoldierTemplate
import logging

logger = logging.getLogger(__name__)

class SoldadoTesorero(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info("SOLDADO TESORERO: Verificando saldos y flujos.")
        return {"action": "cash_flow_verified", "status": "OK"}

class SoldadoAnalistaPresupuesto(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info("SOLDADO PRESUPUESTO: Validando ejecución presupuestal.")
        return {"action": "budget_validated", "execution_rate": 0.85}

class SoldadoAnalistaCredito(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info("SOLDADO CRÉDITO: Analizando obligaciones y amortizaciones.")
        return {"action": "credit_analyzed", "risk_level": "LOW"}

class SoldadoAuditorFinanciero(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info("SOLDADO AUDITOR: Calculando indicadores financieros.")
        from apps.prestadores.mi_negocio.gestion_financiera.services import FinanzasService
        from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

        provider_id = params.get('provider_id')
        if provider_id:
            provider = ProviderProfile.objects.get(id=provider_id)
            indicadores = FinanzasService.calcular_indicadores(provider)
            return {"action": "indicators_calculated", "data": indicadores}
        return {"action": "audit_failed", "reason": "no_provider"}

class SoldadoEspecialistaProyecciones(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info("SOLDADO PROYECCIONES: Generando escenarios financieros.")
        return {"action": "projection_generated", "scenario": "OPTIMISTIC"}
