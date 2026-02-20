from django.db import models
from apps.core_erp.base.base_models import BaseAccount, BaseJournalEntry, BaseAccountingTransaction, BaseFiscalPeriod

class Account(BaseAccount):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        app_label = 'core_erp_accounting'

class FiscalPeriod(BaseFiscalPeriod):
    class Meta:
        app_label = 'core_erp_accounting'

class JournalEntry(BaseJournalEntry):
    period = models.ForeignKey(FiscalPeriod, on_delete=models.PROTECT, related_name='entries')

    class Meta:
        app_label = 'core_erp_accounting'

class Transaction(BaseAccountingTransaction):
    entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='transactions')
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='transactions')

    class Meta:
        app_label = 'core_erp_accounting'
