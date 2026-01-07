from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.core.exceptions import ValidationError
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class CostCenter(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name="cost_centers")
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        app_label = 'contabilidad'

class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.code

    class Meta:
        app_label = 'contabilidad'

class ExchangeRate(models.Model):
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="rates_from")
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="rates_to")
    rate = models.DecimalField(max_digits=18, decimal_places=8)
    date = models.DateField()

    class Meta:
        unique_together = ('from_currency', 'to_currency', 'date')
        app_label = 'contabilidad'

class ChartOfAccount(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name="chart_of_accounts")

    class Nature(models.TextChoices):
        DEBIT = 'DEBITO', 'Debito'
        CREDIT = 'CREDITO', 'Credito'

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    nature = models.CharField(max_length=10, choices=Nature.choices)
    allows_transactions = models.BooleanField(default=True)

    class Meta:
        ordering = ['code']
        unique_together = ('perfil', 'code')
        app_label = 'contabilidad'

    def __str__(self):
        return f"{self.code} - {self.name}"

class JournalEntry(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name="journal_entries")
    entry_date = models.DateField(db_index=True)
    description = models.TextField()
    entry_type = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="journal_entries")
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    origin_document = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-entry_date', '-id']
        app_label = 'contabilidad'

    def __str__(self):
        return f"Asiento #{self.id} del {self.entry_date}"

    def clean(self):
        """
        Valida que la suma de débitos sea igual a la suma de créditos (partida doble).
        Esta validación debe ser llamada explícitamente después de crear el asiento
        y todas sus transacciones asociadas.
        """
        super().clean()
        # La validación solo tiene sentido si el objeto ya existe en la BD y tiene transacciones.
        if self.pk:
            totals = self.transactions.aggregate(
                total_debit=Sum('debit'),
                total_credit=Sum('credit')
            )
            total_debit = totals.get('total_debit') or Decimal('0.00')
            total_credit = totals.get('total_credit') or Decimal('0.00')

            if total_debit != total_credit:
                raise ValidationError(
                    f"El asiento no cumple con la partida doble. Total Débitos: {total_debit}, Total Créditos: {total_credit}"
                )

class Transaction(models.Model):
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name="transactions")
    account = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT)
    debit = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal('0.00'))
    credit = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal('0.00'))
    cost_center = models.ForeignKey(CostCenter, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ['id']
        app_label = 'contabilidad'

    def clean(self):
        if self.debit > 0 and self.credit > 0:
            raise ValidationError("Una transacción no puede tener un valor de débito y crédito a la vez.")
