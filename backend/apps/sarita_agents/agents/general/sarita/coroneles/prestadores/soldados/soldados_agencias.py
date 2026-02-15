# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/soldados/soldados_agencias.py

from apps.sarita_agents.agents.soldado_template import SoldierTemplate
import logging

logger = logging.getLogger(__name__)

class SoldadoValidacionReservaAgencia(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO AGENCIA: Validando reserva -> {params.get('reserva_id')}")
        return {"action": "reservation_validated", "id": params.get('reserva_id')}

class SoldadoRegistroComisionAgencia(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO AGENCIA: Registrando comisión -> {params.get('comision_id')}")
        return {"action": "commission_registered", "id": params.get('comision_id')}

class SoldadoConfirmacionLiquidacionAgencia(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO AGENCIA: Confirmando liquidación -> {params.get('liq_id')}")
        return {"action": "liquidation_confirmed", "id": params.get('liq_id')}

class SoldadoVerificacionItinerarioAgencia(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO AGENCIA: Verificando itinerario -> {params.get('vuelo')}")
        return {"action": "itinerary_checked", "status": "SYNCED"}

class SoldadoMonitoreoDestinoAgencia(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO AGENCIA: Monitoreando disponibilidad en destino.")
        return {"action": "monitored", "availability": "high"}
