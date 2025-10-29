# backend/apps/financiera/models.py
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.prestadores.models import Perfil

class BankAccount(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='bank_accounts')
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    account_holder = models.CharField(max_length=150)

    class AccountType(models.TextChoices):
        SAVINGS = 'SAVINGS', _('Ahorros')
        CHECKING = 'CHECKING', _('Corriente')

    account_type = models.CharField(max_length=10, choices=AccountType.choices)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"

class CashTransaction(models.Model):
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='transactions')

    class TransactionType(models.TextChoices):
        DEPOSIT = 'DEPOSIT', _('Depósito')
        WITHDRAWAL = 'WITHDRAWAL', _('Retiro')
        PAYMENT = 'PAYMENT', _('Pago')

    transaction_type = models.CharField(max_length=10, choices=TransactionType.choices)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='cash_transactions')

    def __str__(self):
        return f"{self.transaction_type} de {self.amount} en {self.bank_account}"
