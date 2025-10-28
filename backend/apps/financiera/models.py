# backend/apps/financiera/models.py
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.prestadores.models import Perfil
from apps.contabilidad.models import ChartOfAccount, JournalEntry

class BankAccount(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='bank_accounts')
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    account_holder = models.CharField(max_length=255)

    class AccountType(models.TextChoices):
        SAVINGS = 'SAVINGS', _('Ahorros')
        CHECKING = 'CHECKING', _('Corriente')

    account_type = models.CharField(max_length=10, choices=AccountType.choices)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    linked_account = models.OneToOneField(
        ChartOfAccount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text=_("Cuenta contable asociada a esta cuenta bancaria (ej. '111005 Bancos')")
    )

    class Meta:
        unique_together = ('perfil', 'account_number', 'bank_name')
        verbose_name = _("Cuenta Bancaria")
        verbose_name_plural = _("Cuentas Bancarias")

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"

class CashTransaction(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='cash_transactions')
    bank_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT)

    class TransactionType(models.TextChoices):
        DEPOSIT = 'DEPOSIT', _('Depósito')
        WITHDRAWAL = 'WITHDRAWAL', _('Retiro')
        TRANSFER = 'TRANSFER', _('Transferencia')

    transaction_type = models.CharField(max_length=10, choices=TransactionType.choices)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    reference = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    journal_entry = models.OneToOneField(
        JournalEntry,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='originating_cash_transaction'
    )

    class Meta:
        verbose_name = _("Transacción de Caja")
        verbose_name_plural = _("Transacciones de Caja")
        ordering = ['-date']

    def __str__(self):
        return f"{self.transaction_type} de {self.amount} en {self.date}"
