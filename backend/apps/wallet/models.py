import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class WalletAccount(models.Model):
    class OwnerType(models.TextChoices):
        TOURIST = "TOURIST", _("Turista")
        PROVIDER = "PROVIDER", _("Prestador")
        DELIVERY = "DELIVERY", _("Delivery")
        EMPLOYEE = "EMPLOYEE", _("Empleado")
        CORPORATE = "CORPORATE", _("Corporativo Interno")

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", _("Activo")
        FROZEN = "FROZEN", _("Congelado")
        BLOCKED = "BLOCKED", _("Bloqueado")
        AUDITED = "AUDITED", _("En Auditoría")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner_type = models.CharField(max_length=20, choices=OwnerType.choices)
    owner_id = models.CharField(max_length=255, help_text="ID del usuario dueño del monedero")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wallets')
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE, related_name='wallets')
    balance = models.DecimalField(max_digits=18, decimal_places=2, default=0.00, help_text="Saldo disponible para transacciones")
    locked_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0.00, help_text="Saldo comprometido en servicios activos")
    currency = models.CharField(max_length=10, default="COP")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Cuenta de Monedero")
        verbose_name_plural = _("Cuentas de Monedero")
        unique_together = ('owner_type', 'owner_id', 'company')

    def __str__(self):
        return f"Wallet {self.owner_type} - {self.user.username} ({self.balance} {self.currency})"

class WalletTransaction(models.Model):
    class TransactionType(models.TextChoices):
        RECHARGE = "RECHARGE", _("Recarga Manual")
        AUTO_RECHARGE = "AUTO_RECHARGE", _("Recarga Automática por Venta")
        DEPOSIT = "DEPOSIT", _("Depósito")
        PAYMENT = "PAYMENT", _("Pago / Débito por Compra")
        TRANSFER = "TRANSFER", _("Transferencia Interna")
        CASHBACK = "CASHBACK", _("Cashback")
        COMMISSION = "COMMISSION", _("Comisión")
        RETENTION = "RETENTION", _("Retención")
        REFUND = "REFUND", _("Reembolso")
        REVERSAL = "REVERSAL", _("Reversión")
        ADJUSTMENT = "ADJUSTMENT", _("Ajuste Administrativo")
        LIQUIDATION = "LIQUIDATION", _("Liquidación")
        FREEZE = "FREEZE", _("Congelamiento")

    class Status(models.TextChoices):
        PENDING = "PENDING", _("Pendiente")
        APPROVED = "APPROVED", _("Aprobado")
        EXECUTED = "EXECUTED", _("Ejecutado")
        REVERSED = "REVERSED", _("Revertido")
        FAILED = "FAILED", _("Fallido")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idempotency_key = models.CharField(max_length=255, unique=True, null=True, blank=True)

    from_wallet = models.ForeignKey(WalletAccount, on_delete=models.PROTECT, related_name='transactions_out', null=True, blank=True)
    to_wallet = models.ForeignKey(WalletAccount, on_delete=models.PROTECT, related_name='transactions_in', null=True, blank=True)

    amount = models.DecimalField(max_digits=18, decimal_places=2)
    type = models.CharField(max_length=20, choices=TransactionType.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    related_service_id = models.UUIDField(null=True, blank=True, help_text="ID del servicio relacionado (Reserva, Pedido, etc.)")
    governance_intention_id = models.CharField(max_length=255, null=True, blank=True, help_text="ID de la intención de gobernanza que autorizó esto")

    description = models.TextField(blank=True)
    metadata = models.JSONField(default=dict, blank=True)

    # Seguridad Fintech
    integrity_hash = models.CharField(max_length=64, null=True, blank=True, help_text="Hash SHA-256 encadenado")
    previous_hash = models.CharField(max_length=64, null=True, blank=True)
    signature = models.TextField(null=True, blank=True, help_text="Firma digital interna")

    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _("Transacción de Monedero")
        verbose_name_plural = _("Transacciones de Monedero")
        ordering = ['-timestamp']

    def __str__(self):
        return f"TX {self.id} - {self.type} - {self.amount}"
