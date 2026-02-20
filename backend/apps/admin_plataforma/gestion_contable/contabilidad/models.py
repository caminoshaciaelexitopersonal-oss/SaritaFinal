import uuid
from django.db import models
from django.conf import settings
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel
from apps.core_erp.base_models import (
    LedgerAccount as BaseAccount, BaseJournalEntry, BaseJournalLine as BaseAccountingTransaction, FinancialPeriod as BaseFiscalPeriod
)

class AdminChartOfAccounts(TenantAwareModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"[ADMIN] Plan: {self.name}"

    class Meta:
        verbose_name = "Plan de Cuentas (Admin)"
        app_label = 'admin_contabilidad'

class AdminAccount(BaseAccount, TenantAwareModel):
    chart_of_accounts = models.ForeignKey(AdminChartOfAccounts, on_delete=models.CASCADE, related_name='admin_accounts')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='admin_children')
    initial_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    class Meta:
        app_label = 'admin_contabilidad'
        unique_together = ('chart_of_accounts', 'code')

class AdminFiscalPeriod(BaseFiscalPeriod, TenantAwareModel):
    class Meta:
        app_label = 'admin_contabilidad'

class AdminJournalEntry(BaseJournalEntry, TenantAwareModel):
    period = models.ForeignKey(AdminFiscalPeriod, on_delete=models.PROTECT, related_name='admin_entries')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='admin_entries_created')

    class Meta:
        app_label = 'admin_contabilidad'

class AdminAccountingTransaction(BaseAccountingTransaction):
    journal_entry = models.ForeignKey(AdminJournalEntry, on_delete=models.CASCADE, related_name='transactions')
    account = models.ForeignKey(AdminAccount, on_delete=models.PROTECT, related_name='transactions')

    class Meta:
        app_label = 'admin_contabilidad'
