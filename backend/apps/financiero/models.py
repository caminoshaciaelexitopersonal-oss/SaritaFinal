# backend/apps/financiero/models.py
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil
from apps.contabilidad.models import ChartOfAccount, JournalEntry

class BankAccount(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='bank_accounts')
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    account_holder = models.CharField(max_length=255)

    class AccountType(models.TextChoices):
        SAVINGS = 'SAVINGS', _('Savings')
        CHECKING = 'CHECKING', _('Checking')

    account_type = models.CharField(max_length=10, choices=AccountType.choices)
    currency = models.ForeignKey('contabilidad.Currency', on_delete=models.PROTECT)
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
        verbose_name = _("Bank Account")
        verbose_name_plural = _("Bank Accounts")

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"

class CashTransaction(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='cash_transactions')
    bank_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT)

    class TransactionType(models.TextChoices):
        DEPOSIT = 'DEPOSIT', _('Deposit')
        WITHDRAWAL = 'WITHDRAWAL', _('Withdrawal')
        TRANSFER = 'TRANSFER', _('Transfer')

    transaction_type = models.CharField(max_length=10, choices=TransactionType.choices)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    reference = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    # Enlace opcional al asiento contable que se genera a partir de esta transacción
    journal_entry = models.OneToOneField(
        JournalEntry,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='originating_cash_transaction'
    )

    class Meta:
        verbose_name = _("Cash Transaction")
        verbose_name_plural = _("Cash Transactions")
        ordering = ['-date']

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.date}"
