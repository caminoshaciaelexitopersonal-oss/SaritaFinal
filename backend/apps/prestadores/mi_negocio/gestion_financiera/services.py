from django.db import transaction as db_transaction
from decimal import Decimal
from datetime import date
from .models import BankAccount, CashTransaction
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import ChartOfAccount
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.services import create_full_journal_entry
from api.models import CustomUser as User

@db_transaction.atomic
def record_cash_movement(
    *,
    user: User,
    bank_account: BankAccount,
    transaction_date: date,
    description: str,
    amount: Decimal,
    contra_account_code: str
) -> CashTransaction:
    """
    Servicio de orquestación para registrar un movimiento de tesorería y su asiento contable
    de forma atómica y validada.
    """
    if amount <= 0:
        raise ValueError("El monto de la transacción debe ser un valor positivo.")

    try:
        contra_account = ChartOfAccount.objects.get(code=contra_account_code, allows_transactions=True)
    except ChartOfAccount.DoesNotExist:
        raise ValueError(f"La contra-cuenta '{contra_account_code}' no existe o no permite transacciones.")

    bank_ledger_account = bank_account.linked_account

    is_inflow = contra_account.nature == ChartOfAccount.Nature.CREDIT

    if is_inflow:
        transaction_type = CashTransaction.TransactionType.INFLOW
        transactions_data = [
            {'account_code': bank_ledger_account.code, 'debit': amount, 'credit': 0},
            {'account_code': contra_account.code, 'debit': 0, 'credit': amount},
        ]
    else:
        transaction_type = CashTransaction.TransactionType.OUTFLOW
        transactions_data = [
            {'account_code': contra_account.code, 'debit': amount, 'credit': 0},
            {'account_code': bank_ledger_account.code, 'debit': 0, 'credit': amount},
        ]

    journal = create_full_journal_entry(
        perfil=user.perfil_prestador,
        user=user,
        entry_date=transaction_date,
        description=description,
        entry_type="Movimiento de Tesorería",
        transactions_data=transactions_data
    )

    cash_transaction = CashTransaction.objects.create(
        bank_account=bank_account,
        transaction_date=transaction_date,
        description=description,
        amount=amount,
        transaction_type=transaction_type,
        status=CashTransaction.Status.PENDING,
        journal_entry=journal,
        created_by=user
    )

    return cash_transaction
