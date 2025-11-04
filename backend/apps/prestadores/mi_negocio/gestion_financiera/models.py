from django.db import models
from django.conf import settings
from decimal import Decimal
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil

class BankAccount(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='bank_accounts')
    name = models.CharField(max_length=255, help_text="Ej: Cuenta Corriente Bancolombia terminada en 1234")
    account_number = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=150)

    # El VÍNCULO MÁS IMPORTANTE
    linked_account = models.OneToOneField(
        'contabilidad.ChartOfAccount',
        on_delete=models.PROTECT,
        help_text="Cuenta contable del PUC asociada a esta cuenta bancaria."
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cuenta Bancaria"
        verbose_name_plural = "Cuentas Bancarias"
        unique_together = ('perfil', 'account_number', 'bank_name')

    def __str__(self):
        return self.name

class CashTransaction(models.Model):
    class TransactionType(models.TextChoices):
        INFLOW = 'INFLOW', 'Ingreso'
        OUTFLOW = 'OUTFLOW', 'Egreso'

    class Status(models.TextChoices):
        PENDING = 'PENDIENTE', 'Pendiente de Conciliar'
        RECONCILED = 'RECONCILIADO', 'Conciliado'

    bank_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name="cash_transactions")
    transaction_date = models.DateField(db_index=True)
    description = models.CharField(max_length=512)
    amount = models.DecimalField(max_digits=18, decimal_places=2, help_text="Valor absoluto.")
    transaction_type = models.CharField(max_length=10, choices=TransactionType.choices, editable=False)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    # Vínculo indestructible al asiento contable
    journal_entry = models.OneToOneField(
        'contabilidad.JournalEntry',
        on_delete=models.PROTECT,
        related_name="cash_transaction"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-transaction_date', '-id']
        verbose_name = "Movimiento de Tesorería"
        verbose_name_plural = "Movimientos de Tesorería"

    def __str__(self):
        return f"{self.transaction_date} | {self.description} | {self.get_transaction_type_display()} de {self.amount}"
