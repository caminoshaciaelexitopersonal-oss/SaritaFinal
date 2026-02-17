# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/soldados/soldados_artesanos.py

from apps.sarita_agents.agents.soldado_template import SoldierTemplate
import logging

logger = logging.getLogger(__name__)

class SoldadoRegistroInventarioArtesano(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO ARTESANO: Registrando inventario -> {params.get('item')}")
        return {"action": "stock_updated", "item": params.get('item')}

class SoldadoValidacionPedidoArtesano(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO ARTESANO: Validando pedido -> {params.get('pedido_id')}")
        return {"action": "order_validated", "id": params.get('pedido_id')}

class SoldadoControlStockArtesano(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO ARTESANO: Control de stock para -> {params.get('categoria')}")
        return {"action": "stock_controlled", "status": "OK"}

class SoldadoConfirmacionDespachoArtesano(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO ARTESANO: Confirmando despacho de -> {params.get('guia')}")
        return {"action": "dispatch_confirmed", "guia": params.get('guia')}

class SoldadoMonitoreoVentasArtesano(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO ARTESANO: Monitoreando ventas del taller.")
        return {"action": "monitored", "trend": "up"}
