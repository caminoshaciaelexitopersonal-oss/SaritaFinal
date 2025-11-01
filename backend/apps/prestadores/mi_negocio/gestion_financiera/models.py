# backend/apps/financiero/models.py
from django.db import models
from django.conf import settings
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil
class BankAccount(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    # currency = models.ForeignKey('contabilidad.Currency', on_delete=models.PROTECT) # Deshabilitado temporalmente
class CashTransaction(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT)
    transaction_type = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    # journal_entry = models.OneToOneField('contabilidad.JournalEntry', on_delete=models.SET_NULL, null=True, blank=True) # Deshabilitado temporalmente
