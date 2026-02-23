from django.db import models
import uuid
from django.utils import timezone

class BaseErpModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CompanyBase(BaseErpModel):
    legal_name = models.CharField(max_length=255, null=True, blank=True)
    tax_id = models.CharField(max_length=50, null=True, blank=True)
    fiscal_regime = models.CharField(max_length=100, null=True, blank=True)
    currency = models.CharField(max_length=3, default='COP')
    country = models.CharField(max_length=100, default='Colombia')

    class Meta:
        abstract = True

class FinancialPeriod(BaseErpModel):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('locked', 'Locked'),
    ]
    period_start = models.DateField(null=True)
    period_end = models.DateField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    class Meta:
        abstract = True

class LedgerAccount(BaseErpModel):
    ACCOUNT_TYPES = [
        ('asset', 'Asset'),
        ('liability', 'Liability'),
        ('equity', 'Equity'),
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    code = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, null=True)
    parent_account = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_accounts')

    class Meta:
        abstract = True

class BaseJournalEntry(BaseErpModel):
    date = models.DateField(default=timezone.now)
    reference = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_posted = models.BooleanField(default=False)
    currency = models.CharField(max_length=3, default='COP')
    exchange_rate = models.DecimalField(max_digits=18, decimal_places=6, default=1.0)

    class Meta:
        abstract = True

class BaseJournalLine(BaseErpModel):
    account_code = models.CharField(max_length=20, null=True, blank=True)
    debit = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    credit = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True

class BaseInvoice(BaseErpModel):
    number = models.CharField(max_length=50, null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, default='DRAFT')
    total_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, default='COP')

    class Meta:
        abstract = True

class BaseInvoiceLine(BaseErpModel):
    description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=2, default=1.00)
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    subtotal = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    class Meta:
        abstract = True

class BaseBankAccount(BaseErpModel):
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.CharField(max_length=50, null=True, blank=True)
    account_type = models.CharField(max_length=50, null=True, blank=True)
    balance = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class BasePayment(BaseErpModel):
    payment_date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    method = models.CharField(max_length=50, null=True, blank=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    bank_fees = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    class Meta:
        abstract = True

class BasePaymentOrder(BaseErpModel):
    payment_date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    concept = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, default='PENDING')

    class Meta:
        abstract = True

class BaseWarehouse(BaseErpModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True

class BaseInventoryMovement(BaseErpModel):
    movement_type = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

class BaseAuditTrail(BaseErpModel):
    action = models.CharField(max_length=100, null=True, blank=True)
    entity_type = models.CharField(max_length=50, null=True, blank=True)
    entity_id = models.UUIDField(null=True)
    payload = models.JSONField(null=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    previous_hash = models.CharField(max_length=64, null=True, blank=True)
    integrity_hash = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        abstract = True

# Compatibility Aliases for existing code
BaseAccount = LedgerAccount
BaseFiscalPeriod = FinancialPeriod
BaseAccountingTransaction = BaseJournalLine
BaseBankTransaction = BasePayment
