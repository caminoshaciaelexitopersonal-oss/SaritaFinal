import logging
from .services import TransportService

logger = logging.getLogger(__name__)

class SargentoTransporte:
    """
    Coordinador de agentes para la operación de Transporte Turístico.
    """
    @staticmethod
    def programar_y_asignar(parametros, user):
        service = TransportService(user)

        if "nuevo_estado" in parametros:
            trip = service.actualizar_estado_viaje(parametros['trip_id'], parametros['nuevo_estado'])
            return {"status": "SUCCESS", "trip_id": str(trip.id), "estado": trip.estado}

        trip = service.programar_viaje(parametros)
        return {"status": "SUCCESS", "trip_id": str(trip.id)}

    @staticmethod
    def registrar_reserva_masiva(parametros, user):
        service = TransportService(user)
        reserva = service.registrar_reserva(parametros['trip_id'], parametros)
        return {"status": "SUCCESS", "booking_id": str(reserva.id)}

    @staticmethod
    def liquidar_servicio_transporte(parametros, user):
        service = TransportService(user)
        liq = service.liquidar_viaje(parametros['trip_id'])
        return {"status": "SUCCESS", "liquidation_id": str(liq.id)}
