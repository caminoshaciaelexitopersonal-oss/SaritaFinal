# backend/apps/contabilidad/services.py
from django.db import transaction
from .models import JournalEntry, Transaction, ChartOfAccount
def create_full_journal_entry(perfil, date, description, transactions_data, created_by):
    with transaction.atomic():
        journal_entry = JournalEntry.objects.create(perfil=perfil, date=date, description=description, created_by=created_by)
        for t_data in transactions_data:
            account = ChartOfAccount.objects.get(perfil=perfil, account_number=t_data['account_number'])
            Transaction.objects.create(journal_entry=journal_entry, account=account, debit=t_data.get('debit', 0), credit=t_data.get('credit', 0))
    return journal_entry
