import logging
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import transaction

logger = logging.getLogger(__name__)

class TreasuryEngine:
    """
    Motor de tesorería centralizado.
    Gestiona movimientos de caja, bancos y estados de pago.
    """

    @staticmethod
    def validate_bank_transaction(transaction):
        if transaction.amount == 0:
            raise ValidationError("El monto de la transacción bancaria no puede ser cero.")

    @staticmethod
    @transaction.atomic
    def process_payment(payment_order, bank_account):
        """
        Procesa una orden de pago contra una cuenta bancaria.
        """
        if payment_order.amount > bank_account.balance:
            raise ValidationError("Saldo insuficiente en la cuenta bancaria.")

        bank_account.balance -= payment_order.amount
        bank_account.save()

        payment_order.status = 'PAID'
        payment_order.save()

        logger.info(f"Pago {payment_order.id} procesado exitosamente. Nuevo saldo: {bank_account.balance}")
        return payment_order
