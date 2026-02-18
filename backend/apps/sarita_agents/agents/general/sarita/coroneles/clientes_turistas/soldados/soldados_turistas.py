# backend/apps/sarita_agents/agents/general/sarita/coroneles/clientes_turistas/soldados/soldados_turistas.py

from apps.sarita_agents.agents.soldado_template import SoldierTemplate
import logging

logger = logging.getLogger(__name__)

class SoldadoBuscadorServicios(SoldierTemplate):
    """Busca servicios disponibles basados en preferencias del turista."""
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO TURISTA: Buscando -> {params.get('query')}")
        return {"status": "RESULTS_FOUND", "count": 12}

class SoldadoGestorReservas(SoldierTemplate):
    """Ejecuta y confirma reservas para el turista."""
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO TURISTA: Reservando -> {params.get('servicio_id')}")
        return {"status": "RESERVED", "reserva_id": "RES-999"}

class SoldadoSoportePQRS(SoldierTemplate):
    """Atiende y clasifica quejas o reclamos del turista."""
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO TURISTA: Procesando PQRS -> {params.get('asunto')}")
        return {"status": "FILED", "radicado": "RAD-2024-001"}
