# backend/apps/financiero/services.py
from django.db import transaction
from .models import CashTransaction
from apps.prestadores.mi_negocio.gestion_contable.services import create_full_journal_entry
def create_cash_transaction_with_accounting(perfil, bank_account, transaction_type, amount, date, description, created_by, **kwargs):
    with transaction.atomic():
        if transaction_type == 'DEPOSIT': bank_account.balance += amount
        else: bank_account.balance -= amount
        bank_account.save()
        cash_tx = CashTransaction.objects.create(perfil=perfil, bank_account=bank_account, transaction_type=transaction_type, amount=amount, date=date, description=description, created_by=created_by)
        if kwargs.get('generate_journal_entry'):
            journal_entry = create_full_journal_entry(perfil=perfil, date=date, description=f"Asiento por {description}", created_by=created_by, transactions_data=[{'account_number': kwargs['debit_account_number'], 'debit': amount}, {'account_number': kwargs['credit_account_number'], 'credit': amount}])
            cash_tx.journal_entry = journal_entry
            cash_tx.save()
    return cash_tx
