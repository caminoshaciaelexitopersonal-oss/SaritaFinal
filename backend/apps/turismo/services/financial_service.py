import logging
from decimal import Decimal
from django.db import transaction
from apps.wallet.services import WalletService
from ..models.provider_models import TourismProvider, Reservation

logger = logging.getLogger(__name__)

class TourismFinancialService:
    """
    Orquesta la integración financiera entre el Dominio Turismo y el Wallet.
    """

    @staticmethod
    @transaction.atomic
    def process_reservation_payment(reservation_id: str):
        """
        Ejecuta el pago de una reserva: de Turista a Prestador.
        """
        reservation = Reservation.objects.get(id=reservation_id)
        if reservation.status != Reservation.Status.PENDING:
            raise ValueError("La reserva no está en estado pendiente para pago.")

        # Obtener el owner del proveedor (Prestador)
        prestador_user = reservation.provider.owner

        # Inicializar WalletService para el cliente (Turista)
        wallet_service = WalletService(user=reservation.customer)

        # Ejecutar el pago
        try:
            transaction_res = wallet_service.pay_to_user(
                target_user=prestador_user,
                amount=reservation.total_price,
                related_service_id=str(reservation.service.id),
                description=f"Pago Reserva {reservation.id} - {reservation.service.name}"
            )

            # Actualizar estado de la reserva
            reservation.status = Reservation.Status.CONFIRMED
            reservation.metadata['wallet_transaction_id'] = str(transaction_res.id)
            reservation.save()

            logger.info(f"Pago procesado exitosamente para reserva {reservation.id}")
            return transaction_res

        except Exception as e:
            logger.error(f"Error al procesar pago de reserva {reservation.id}: {e}")
            raise e

    @staticmethod
    def get_provider_balance(provider_id: str):
        """
        Consulta el saldo disponible del prestador en su wallet.
        """
        provider = TourismProvider.objects.get(id=provider_id)
        wallet_service = WalletService(user=provider.owner)
        return wallet_service.get_wallet_balance()
