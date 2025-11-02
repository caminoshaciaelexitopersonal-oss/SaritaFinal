from django.db import models
from django.conf import settings
from decimal import Decimal
from apps.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil
from apps.contabilidad.models import ChartOfAccount, JournalEntry

class BankAccount(models.Model):
    """
    Representa una cuenta bancaria física de un prestador.
    """
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='cuentas_bancarias')
    nombre = models.CharField(max_length=255, help_text="Ej: Cuenta Corriente Bancolombia")
    numero_cuenta = models.CharField(max_length=50)
    nombre_banco = models.CharField(max_length=150)
    # Asumo una moneda por defecto o podría añadirse una ForeignKey a un modelo Currency

    cuenta_contable_asociada = models.OneToOneField(
        ChartOfAccount,
        on_delete=models.PROTECT,
        help_text="Cuenta contable del PUC que representa este banco."
    )
    esta_activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cuenta Bancaria"
        verbose_name_plural = "Cuentas Bancarias"
        unique_together = ('perfil', 'numero_cuenta', 'nombre_banco')

    def __str__(self):
        return self.nombre

class CashTransaction(models.Model):
    """
    Representa un movimiento individual de dinero para un prestador.
    """
    class TransactionType(models.TextChoices):
        INFLOW = 'INFLOW', 'Ingreso'
        OUTFLOW = 'OUTFLOW', 'Egreso'

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='transacciones_caja')
    cuenta_bancaria = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name="transacciones")
    fecha_transaccion = models.DateField(db_index=True)
    descripcion = models.CharField(max_length=512)
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    tipo_transaccion = models.CharField(max_length=10, choices=TransactionType.choices)

    asiento_contable = models.OneToOneField(
        JournalEntry,
        on_delete=models.PROTECT,
        related_name="transaccion_caja"
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_transaccion', '-id']
        verbose_name = "Movimiento de Tesorería"
        verbose_name_plural = "Movimientos de Tesorería"

    def __str__(self):
        return f"{self.fecha_transaccion} | {self.descripcion} | {self.get_tipo_transaccion_display()} de {self.monto}"
