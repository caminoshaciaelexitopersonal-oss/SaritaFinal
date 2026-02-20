import logging
from django.core.exceptions import ValidationError
from django.db import transaction

logger = logging.getLogger(__name__)

class AccountingEngine:
    """
    Motor contable centralizado para validación y procesamiento de asientos.
    """

    @staticmethod
    def validate_balance(entry):
        """
        Valida que un asiento esté balanceado (Debe = Haber).
        """
        # Usamos el related_name 'transactions' estandarizado
        transactions = entry.transactions.all()
        total_debit = sum(t.debit for t in transactions)
        total_credit = sum(t.credit for t in transactions)

        if total_debit != total_credit:
             raise ValidationError(f"Asiento descuadrado: Débito ({total_debit}) != Crédito ({total_credit})")

        return True

    @staticmethod
    @transaction.atomic
    def post_entry(entry):
        """
        Realiza el registro definitivo de un asiento contable (Paso 3).
        """
        if entry.is_posted:
             raise ValidationError("El asiento ya ha sido contabilizado.")

        AccountingEngine.validate_balance(entry)

        entry.is_posted = True
        entry.save()
        logger.info(f"Asiento {entry.id} contabilizado exitosamente via Engine.")
        return entry
