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
        reservation = Reservation.objects.get(id=reservation_id)

        if not reservation.service.delivery_available:
            raise ValueError(f"El servicio {reservation.service.name} no tiene delivery disponible.")

        logistic_service = DeliveryLogisticService(user=reservation.customer)

        parameters = {
            "origin_address": origin_address,
            "destination_address": destination_address,
            "estimated_price": 5000,
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

        delivery_request = logistic_service.create_request(parameters)
        reservation.metadata['delivery_request_id'] = str(delivery_request.id)
        reservation.save()

        return delivery_request

    @staticmethod
    def create_delivery(provider, customer, items, address):
        """
        Crea un pedido de delivery directo.
        """
        logistic_service = DeliveryLogisticService(user=customer)
        parameters = {
            "origin_address": "Sede Prestador",
            "destination_address": address,
            "provider_id": str(provider.id),
            "items": items
        }
        return logistic_service.create_request(parameters)
