import logging
from decimal import Decimal
from django.db import transaction
from apps.wallet.services import WalletService
from ..models.provider_models import TourismProvider, Reservation, TourismService

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

        prestador_user = reservation.provider.owner
        wallet_service = WalletService(user=reservation.customer)

        try:
            transaction_res = wallet_service.pay_to_user(
                target_user=prestador_user,
                amount=reservation.total_price,
                related_service_id=str(reservation.service.id),
                description=f"Pago Reserva {reservation.id} - {reservation.service.name}"
            )

            reservation.status = Reservation.Status.CONFIRMED
            reservation.metadata['wallet_transaction_id'] = str(transaction_res.id)
            reservation.save()

            logger.info(f"Pago procesado exitosamente para reserva {reservation.id}")
            return transaction_res

        except Exception as e:
            logger.error(f"Error al procesar pago de reserva {reservation.id}: {e}")
            raise e

    @staticmethod
    def register_transaction(provider, amount, customer, description="Venta Directa"):
        """
        Registra una transacción directa sin reserva previa (POS).
        """
        wallet_service = WalletService(user=customer)
        return wallet_service.pay_to_user(
            target_user=provider.owner,
            amount=amount,
            description=description
        )

    @staticmethod
    def calculate_commission(amount, percentage=Decimal('0.10')):
        """
        Calcula la comisión para la plataforma.
        """
        return (amount * percentage).quantize(Decimal('0.01'))

    @staticmethod
    def get_provider_balance(provider_id: str):
        provider = TourismProvider.objects.get(id=provider_id)
        wallet_service = WalletService(user=provider.owner)
        return wallet_service.get_wallet_balance()
