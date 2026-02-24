from django.db import models
from django.conf import settings
from apps.core_erp.base_models import (
    BaseErpModel, TenantAwareModel, LedgerAccount as BaseAccount,
    BaseJournalEntry, BaseJournalLine as BaseJournalLineBase,
    FinancialPeriod as BaseFinancialPeriod
)

class AccountingTenantModel(TenantAwareModel):
    class Meta:
        abstract = True

class ChartOfAccounts(AccountingTenantModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.tenant})"

    class Meta:
        app_label = 'core_erp'
        verbose_name = "Chart of Accounts"

class Account(BaseAccount, AccountingTenantModel):
    # BaseAccount has code, name, type, parent_account
    chart_of_accounts = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE, related_name='accounts')
    initial_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)

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
    # BaseJournalEntry has date, reference, description, is_posted
    period = models.ForeignKey(FiscalPeriod, on_delete=models.PROTECT, related_name='entries')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    event_type = models.CharField(max_length=100, null=True, blank=True)
    is_reversal = models.BooleanField(default=False)
    reversed_entry_id = models.UUIDField(null=True, blank=True)

    class Meta:
        app_label = 'core_erp'
        verbose_name = "Journal Entry"

class LedgerEntry(TenantAwareModel):
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='lines')
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='ledger_entries')
    debit_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    credit_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, default='COP')
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'core_erp'
        verbose_name = "Ledger Entry"
