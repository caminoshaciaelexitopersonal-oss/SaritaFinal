# backend/apps/financiero/services.py
from django.db import transaction
from django.core.exceptions import ValidationError
from .models import CashTransaction, BankAccount
from apps.contabilidad.services import create_full_journal_entry

def create_cash_transaction_with_accounting(
    perfil,
    bank_account,
    transaction_type,
    amount,
    date,
    description,
    created_by,
    debit_account_number,
    credit_account_number,
    generate_journal_entry=True
):
    """
    Crea una transacción de tesorería y, si se indica, su asiento contable correspondiente.

    Args:
        perfil (Perfil): El perfil del prestador.
        bank_account (BankAccount): La cuenta bancaria afectada.
        transaction_type (str): 'DEPOSIT', 'WITHDRAWAL', etc.
        amount (Decimal): Monto de la transacción.
        date (date): Fecha de la transacción.
        description (str): Descripción.
        created_by (User): Usuario que realiza la operación.
        debit_account_number (str): Número de la cuenta contable a debitar.
        credit_account_number (str): Número de la cuenta contable a acreditar.
        generate_journal_entry (bool): Si es True, crea el asiento contable.

    Returns:
        CashTransaction: La transacción de tesorería creada.
    """
    with transaction.atomic():
        # 1. Actualizar el saldo de la cuenta bancaria
        if transaction_type == CashTransaction.TransactionType.DEPOSIT:
            bank_account.balance += amount
        elif transaction_type == CashTransaction.TransactionType.WITHDRAWAL:
            if bank_account.balance < amount:
                raise ValidationError("Saldo insuficiente en la cuenta bancaria.")
            bank_account.balance -= amount
        # (La lógica para 'TRANSFER' sería más compleja y se omite por simplicidad aquí)

        bank_account.save()

        # 2. Crear la transacción de tesorería
        cash_transaction = CashTransaction.objects.create(
            perfil=perfil,
            bank_account=bank_account,
            transaction_type=transaction_type,
            amount=amount,
            date=date,
            description=description,
            created_by=created_by,
        )

        # 3. Opcionalmente, crear el asiento contable
        if generate_journal_entry:
            journal_description = f"Asiento por {transaction_type.lower()}: {description}"

            transactions_data = [
                {'account_number': debit_account_number, 'debit': amount, 'credit': 0},
                {'account_number': credit_account_number, 'debit': 0, 'credit': amount},
            ]

            journal_entry = create_full_journal_entry(
                perfil=perfil,
                date=date,
                description=journal_description,
                transactions_data=transactions_data,
                created_by=created_by
            )

            # Enlazar el asiento con la transacción
            cash_transaction.journal_entry = journal_entry
            cash_transaction.save()

    return cash_transaction
