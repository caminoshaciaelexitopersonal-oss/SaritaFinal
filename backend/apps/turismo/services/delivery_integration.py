import logging
from django.db import transaction
from apps.delivery.services import DeliveryLogisticService
from ..models.provider_models import TourismProvider, Reservation, TourismService

logger = logging.getLogger(__name__)

class TourismDeliveryService:
    """
    Orquesta la integración logística entre el Dominio Turismo y el Delivery.
    """

    @staticmethod
    @transaction.atomic
    def request_delivery_for_reservation(reservation_id: str, origin_address: str, destination_address: str):
        """
        Crea una solicitud de delivery asociada a una reserva confirmada.
        """
        reservation = Reservation.objects.get(id=reservation_id)

        # Validar que el servicio permita delivery
        if not reservation.service.delivery_available:
            raise ValueError(f"El servicio {reservation.service.name} no tiene delivery disponible.")

        # Inicializar Delivery Service para el cliente
        logistic_service = DeliveryLogisticService(user=reservation.customer)

        # Parámetros para la solicitud
        parameters = {
            "origin_address": origin_address,
            "destination_address": destination_address,
            "estimated_price": 5000, # Valor base simulado
            "value_declared": float(reservation.total_price),
            "related_operational_order_id": str(reservation.id),
            "provider_id": str(reservation.provider.id),
            "items": [
                {
                    "description": f"Servicio Turístico: {reservation.service.name}",
                    "quantity": 1,
                    "weight_kg": 1.0
                }
            ]
        }

        try:
            delivery_request = logistic_service.create_request(parameters)

            # Vincular en metadata de la reserva
            reservation.metadata['delivery_request_id'] = str(delivery_request.id)
            reservation.save()

            logger.info(f"Solicitud de delivery {delivery_request.id} creada para reserva {reservation.id}")
            return delivery_request

        except Exception as e:
            logger.error(f"Error al crear solicitud de delivery para reserva {reservation.id}: {e}")
            raise e
