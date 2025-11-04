from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil

# TODO: Importar ClosingPeriod cuando el módulo exista
# from close_process.models import ClosingPeriod

class CostCenter(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="cost_centers")
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Centro de Costo"
        verbose_name_plural = "Centros de Costo"

    def __str__(self):
        return f"{self.code} - {self.name}"

class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True, help_text="Código ISO 4217, ej. 'COP', 'USD'")
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"

    def __str__(self):
        return self.code

class ExchangeRate(models.Model):
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="rates_from")
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="rates_to")
    rate = models.DecimalField(max_digits=18, decimal_places=8)
    date = models.DateField()

    class Meta:
        unique_together = ('from_currency', 'to_currency', 'date')
        verbose_name = "Tasa de Cambio"
        verbose_name_plural = "Tasas de Cambio"

class ChartOfAccount(models.Model):
    class Nature(models.TextChoices):
        DEBIT = 'DEBITO', 'Debito'
        CREDIT = 'CREDITO', 'Credito'

    code = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    nature = models.CharField(max_length=10, choices=Nature.choices)
    allows_transactions = models.BooleanField(default=True, help_text="Si es 'False', es una cuenta de control y no puede recibir asientos.")

    class Meta:
        ordering = ['code']
        verbose_name = "Cuenta Contable"
        verbose_name_plural = "Plan de Cuentas (PUC)"

    def __str__(self):
        return f"{self.code} - {self.name}"

class JournalEntry(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="journal_entries")
    entry_date = models.DateField(db_index=True)
    description = models.TextField()
    entry_type = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="accounting_journal_entries")

    # Trazabilidad con otros módulos (vínculo genérico)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    origin_document = GenericForeignKey('content_type', 'object_id')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-entry_date', '-id']
        verbose_name = "Asiento Contable"
        verbose_name_plural = "Asientos Contables (Libro Diario)"

    def clean(self):
        super().clean()
        # TODO: Implementar validación de período cerrado cuando el modelo ClosingPeriod exista.
        # if self.pk is None:
        #     is_period_closed = ClosingPeriod.objects.filter(
        #         perfil=self.perfil,
        #         period_year=self.entry_date.year,
        #         period_month=self.entry_date.month,
        #         status=ClosingPeriod.Status.CLOSED
        #     ).exists()
        #     if is_period_closed:
        #         raise ValidationError(f"El período {self.entry_date.strftime('%Y-%m')} está cerrado.")

    def __str__(self):
        return f"Asiento #{self.id} del {self.entry_date}"

class Transaction(models.Model):
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name="transactions")
    account = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT)
    debit = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal('0.00'))
    credit = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal('0.00'))

    # Dimensiones de análisis
    cost_center = models.ForeignKey(CostCenter, on_delete=models.PROTECT, null=True, blank=True)
    # TODO: Añadir ForeignKey a 'projects.Project' cuando el módulo exista.
    # project = models.ForeignKey('projects.Project', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = "Transacción Contable"
        verbose_name_plural = "Transacciones Contables"

    def clean(self):
        if self.debit > 0 and self.credit > 0:
            raise ValidationError("Una transacción no puede tener un valor de débito y crédito a la vez.")
