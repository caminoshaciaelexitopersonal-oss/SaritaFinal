import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class WalletAccount(models.Model):
    class OwnerType(models.TextChoices):
        TOURIST = "TOURIST", _("Turista")
        PROVIDER = "PROVIDER", _("Prestador")
        DELIVERY = "DELIVERY", _("Delivery")

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", _("Activo")
        FROZEN = "FROZEN", _("Congelado")
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
        DEPOSIT = "DEPOSIT", _("Depósito")
        PAYMENT = "PAYMENT", _("Pago")
        REFUND = "REFUND", _("Reembolso")
        ADJUSTMENT = "ADJUSTMENT", _("Ajuste")
        LIQUIDATION = "LIQUIDATION", _("Liquidación")

    class Status(models.TextChoices):
        PENDING = "PENDING", _("Pendiente")
        APPROVED = "APPROVED", _("Aprobado")
        EXECUTED = "EXECUTED", _("Ejecutado")
        REVERSED = "REVERSED", _("Revertido")
        FAILED = "FAILED", _("Fallido")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_wallet = models.ForeignKey(WalletAccount, on_delete=models.PROTECT, related_name='transactions_out', null=True, blank=True)
    to_wallet = models.ForeignKey(WalletAccount, on_delete=models.PROTECT, related_name='transactions_in', null=True, blank=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    type = models.CharField(max_length=20, choices=TransactionType.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    related_service_id = models.UUIDField(null=True, blank=True, help_text="ID del servicio relacionado (Reserva, Pedido, etc.)")
    governance_intention_id = models.CharField(max_length=255, null=True, blank=True, help_text="ID de la intención de gobernanza que autorizó esto")

    description = models.TextField(blank=True)
    metadata = models.JSONField(default=dict, blank=True)

    integrity_hash = models.CharField(max_length=64, null=True, blank=True, help_text="Hash encadenado para integridad forense")
    previous_hash = models.CharField(max_length=64, null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Transacción de Monedero")
        verbose_name_plural = _("Transacciones de Monedero")
        ordering = ['-timestamp']

    def __str__(self):
        return f"TX {self.id} - {self.type} - {self.amount}"
