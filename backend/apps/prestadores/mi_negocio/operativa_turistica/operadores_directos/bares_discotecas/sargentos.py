import logging
from .services import NightclubService
from apps.sarita_agents.models import MicroTarea

logger = logging.getLogger(__name__)

class SargentoNocturno:
    """
    Coordinador de agentes para Bares y Discotecas.
    """
    @staticmethod
    def procesar_comanda(parametros, user):
        service = NightclubService(user)
        consumption = service.registrar_consumo(
            parametros['consumption_id'],
            parametros['items']
        )
        return {"status": "SUCCESS", "consumption_id": str(consumption.id)}

    @staticmethod
    def facturar_mesa(parametros, user):
        service = NightclubService(user)
        impact = service.facturar_consumo(parametros['consumption_id'])
        return {"status": "SUCCESS", "erp_impact": impact}

    @staticmethod
    def cerrar_caja(parametros, user):
        service = NightclubService(user)
        closing = service.cierre_caja(parametros['event_id'], parametros)
        return {"status": "SUCCESS", "closing_id": str(closing.id)}

    @staticmethod
    def anular_consumo(parametros, user):
        service = NightclubService(user)
        consumption = service.anular_consumo(
            parametros['consumption_id'],
            parametros.get('motivo', 'Anulación por agente')
        )
        return {"status": "SUCCESS", "consumption_id": str(consumption.id)}
