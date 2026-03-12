import logging
from .services import AgencyService

logger = logging.getLogger(__name__)

class SargentoAgencia:
    """
    Coordinador de agentes para la operación de Agencia de Viajes (Consolidación).
    """
    @staticmethod
    def crear_paquete_turistico(parametros, user):
        service = AgencyService(user)
        package = service.crear_paquete(parametros)
        return {"status": "SUCCESS", "package_id": str(package.id), "precio_total": float(package.precio_total)}

    @staticmethod
    def reservar_paquete_consolidado(parametros, user):
        service = AgencyService(user)
        booking = service.registrar_reserva_paquete(parametros['package_id'], parametros)
        return {"status": "SUCCESS", "booking_id": str(booking.id), "total": float(booking.total_facturado)}

    @staticmethod
    def cancelar_componente_paquete(parametros, user):
        service = AgencyService(user)
        booking = service.cancelar_componente_parcial(parametros['booking_id'], parametros['component_id'])
        return {"status": "SUCCESS", "new_total": float(booking.total_facturado)}

    @staticmethod
    def liquidar_agencia(parametros, user):
        service = AgencyService(user)
        liq = service.liquidar_paquete(parametros['booking_id'])
        return {
            "status": "SUCCESS",
            "liquidation_id": str(liq.id),
            "utilidad": float(liq.utilidad_agencia)
        }
