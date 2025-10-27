# backend/apps/contabilidad/models.py
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil

class CostCenter(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='cost_centers')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.code})"

class ChartOfAccount(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='chart_of_accounts')
    account_number = models.CharField(max_length=20)
    name = models.CharField(max_length=255)

    class AccountType(models.TextChoices):
        ASSET = 'ASSET', _('Asset')
        LIABILITY = 'LIABILITY', _('Liability')
        EQUITY = 'EQUITY', _('Equity')
        REVENUE = 'REVENUE', _('Revenue')
        EXPENSE = 'EXPENSE', _('Expense')

    account_type = models.CharField(max_length=10, choices=AccountType.choices)
    is_active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        unique_together = ('perfil', 'account_number')
        verbose_name = _("Chart of Account")
        verbose_name_plural = _("Charts of Accounts")

    def __str__(self):
        return f"{self.account_number} - {self.name}"

class JournalEntry(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='journal_entries')
    date = models.DateField()
    description = models.TextField()
    cost_center = models.ForeignKey(CostCenter, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='journal_entries_created')

    def __str__(self):
        return f"JE-{self.id} on {self.date}"

    def clean(self):
        super().clean()
        transactions = self.transactions.all()
        total_debit = sum(t.debit for t in transactions)
        total_credit = sum(t.credit for t in transactions)
        if total_debit != total_credit:
            raise ValidationError(_('The total debit and credit for a journal entry must be equal.'))

class Transaction(models.Model):
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='transactions')
    account = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Transaction {self.id} for JE-{self.journal_entry.id}"

    def clean(self):
        super().clean()
        if self.debit > 0 and self.credit > 0:
            raise ValidationError(_('A transaction cannot have both debit and credit.'))
        if self.debit == 0 and self.credit == 0:
            raise ValidationError(_('A transaction must have either a debit or a credit.'))
