# backend/apps/contabilidad/models.py
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import ValidationError
from decimal import Decimal

# Importación clave para vincular los datos al prestador
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil

# NOTA: Por ahora, se comentan las dependencias a otros módulos que aún no hemos creado
# para asegurar que las migraciones iniciales funcionen.
# from closing_process.models import ClosingPeriod
# from projects.models import Project

class CostCenter(models.Model):
    """Dimensión de análisis: Centros de Costo."""
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="cost_centers")
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Centro de Costo"
        verbose_name_plural = "Centros de Costo"
        unique_together = ('perfil', 'code') # El código es único por prestador

    def __str__(self):
        return f"{self.code} - {self.name}"

class Currency(models.Model):
    """Define las monedas que el sistema puede manejar (Modelo Global)."""
    code = models.CharField(max_length=3, primary_key=True, help_text="Código ISO 4217, ej. 'COP', 'USD'")
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"

    def __str__(self):
        return self.code

class ExchangeRate(models.Model):
    """Almacena las tasas de cambio (Modelo Global)."""
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="rates_from")
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="rates_to")
    rate = models.DecimalField(max_digits=18, decimal_places=8)
    date = models.DateField()

    class Meta:
        unique_together = ('from_currency', 'to_currency', 'date')
        verbose_name = "Tasa de Cambio"
        verbose_name_plural = "Tasas de Cambio"

class ChartOfAccount(models.Model):
    """El Plan de Cuentas (PUC), la columna vertebral del sistema."""
    class Nature(models.TextChoices):
        DEBIT = 'DEBITO', 'Debito'
        CREDIT = 'CREDITO', 'Credito'

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="chart_of_accounts")
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    nature = models.CharField(max_length=10, choices=Nature.choices)
    allows_transactions = models.BooleanField(default=True, help_text="Si es 'False', es una cuenta de control y no puede recibir asientos.")

    class Meta:
        ordering = ['code']
        verbose_name = "Cuenta Contable"
        verbose_name_plural = "Plan de Cuentas (PUC)"
        unique_together = ('perfil', 'code')

    def __str__(self):
        return f"{self.code} - {self.name}"

class JournalEntry(models.Model):
    """El encabezado de un asiento contable."""
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="journal_entries")
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
        verbose_name = "Asiento Contable"
        verbose_name_plural = "Asientos Contables (Libro Diario)"

    def __str__(self):
        return f"Asiento #{self.id} del {self.entry_date}"

class Transaction(models.Model):
    """Una línea (movimiento) dentro de un asiento contable."""
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name="transactions")
    account = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT)

    debit = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal('0.00'))
    credit = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal('0.00'))

    cost_center = models.ForeignKey(CostCenter, on_delete=models.PROTECT, null=True, blank=True)
    # project = models.ForeignKey('projects.Project', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = "Transacción Contable"
        verbose_name_plural = "Transacciones Contables"

    def clean(self):
        if self.debit > 0 and self.credit > 0:
            raise ValidationError("Una transacción no puede tener un valor de débito y crédito a la vez.")
