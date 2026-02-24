from django.db import models
from django.conf import settings
from apps.core_erp.base_models import (
    BaseErpModel, LedgerAccount as BaseAccount, BaseJournalEntry,
    BaseJournalLine as BaseJournalLineBase, FinancialPeriod as BaseFinancialPeriod
)

class AccountingTenantModel(BaseErpModel):
    organization_id = models.UUIDField(db_index=True)

    class Meta:
        abstract = True

class ChartOfAccounts(AccountingTenantModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.organization_id})"

    class Meta:
        app_label = 'core_erp'
        verbose_name = "Chart of Accounts"

class Account(BaseAccount, AccountingTenantModel):
    chart_of_accounts = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE, related_name='accounts')
    initial_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    class Meta:
        app_label = 'core_erp'
        unique_together = ('chart_of_accounts', 'code')

    def __str__(self):
        return f"{self.code} - {self.name}"

class FiscalPeriod(BaseFinancialPeriod, AccountingTenantModel):
    class Meta:
        app_label = 'core_erp'
        verbose_name = "Fiscal Period"

class JournalEntry(BaseJournalEntry, AccountingTenantModel):
    period = models.ForeignKey(FiscalPeriod, on_delete=models.PROTECT, related_name='entries')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'core_erp'
        verbose_name = "Journal Entry"

class JournalLine(BaseJournalLineBase, BaseErpModel):
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='lines')
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='journal_lines')

    class Meta:
        app_label = 'core_erp'
        verbose_name = "Journal Line"
