from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from decimal import Decimal
from apps.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil

class ChartOfAccount(models.Model):
    """El Plan de Cuentas (PUC), adaptado para Sarita."""
    class Nature(models.TextChoices):
        DEBIT = 'DEBITO', 'Debito'
        CREDIT = 'CREDITO', 'Credito'

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='plan_de_cuentas')
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=255)
    naturaleza = models.CharField(max_length=10, choices=Nature.choices)
    permite_transacciones = models.BooleanField(default=True, help_text="Si es 'False', es una cuenta de control.")

    class Meta:
        ordering = ['codigo']
        verbose_name = "Cuenta Contable"
        verbose_name_plural = "Plan de Cuentas (PUC)"
        unique_together = ('perfil', 'codigo')

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class JournalEntry(models.Model):
    """El encabezado de un asiento contable para un prestador."""
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='asientos_contables')
    entry_date = models.DateField(db_index=True)
    description = models.TextField()
    entry_type = models.CharField(max_length=100)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="asientos_creados")
    creado_en = models.DateTimeField(auto_now_add=True)

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

    class Meta:
        ordering = ['id']
        verbose_name = "Transacción Contable"
        verbose_name_plural = "Transacciones Contables"

    def clean(self):
        if self.debit > 0 and self.credit > 0:
            raise ValidationError("Una transacción no puede tener un valor de débito y crédito a la vez.")
