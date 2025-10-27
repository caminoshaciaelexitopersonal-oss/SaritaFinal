# backend/apps/contabilidad/models.py
from django.db import models
from django.conf import settings
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil
class CostCenter(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
class ChartOfAccount(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    class Meta: unique_together = ('perfil', 'account_number')
class JournalEntry(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
class Transaction(models.Model):
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='transactions')
    account = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
