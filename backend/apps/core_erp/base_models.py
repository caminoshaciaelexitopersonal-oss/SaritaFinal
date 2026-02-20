from django.db import models
import uuid

class BaseErpModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CompanyBase(BaseErpModel):
    """
    Base model for any legal entity in the system.
    """
    legal_name = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=50)
    fiscal_regime = models.CharField(max_length=100)
    currency = models.CharField(max_length=3, default='COP')
    country = models.CharField(max_length=100, default='Colombia')

    class Meta:
        abstract = True

class FinancialPeriod(BaseErpModel):
    """
    Definition of an accounting/fiscal period.
    """
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('locked', 'Locked'),
    ]
    period_start = models.DateField()
    period_end = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    class Meta:
        abstract = True

class LedgerAccount(BaseErpModel):
    """
    Standard Ledger Account (PUC).
    """
    ACCOUNT_TYPES = [
        ('asset', 'Asset'),
        ('liability', 'Liability'),
        ('equity', 'Equity'),
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    parent_account = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_accounts')

    class Meta:
        abstract = True

class BaseJournalEntry(BaseErpModel):
    date = models.DateField()
    reference = models.CharField(max_length=255)
    description = models.TextField()
    is_posted = models.BooleanField(default=False)
    currency = models.CharField(max_length=3, default='COP')
    exchange_rate = models.DecimalField(max_digits=18, decimal_places=6, default=1.0)

    class Meta:
        abstract = True

class BaseJournalLine(BaseErpModel):
    account_code = models.CharField(max_length=20)
    debit = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    credit = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True

class BaseInvoice(BaseErpModel):
    number = models.CharField(max_length=50)
    issue_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=30, default='DRAFT')
    total_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, default='COP')

    class Meta:
        abstract = True

class BaseInvoiceLine(BaseErpModel):
    description = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=18, decimal_places=2, default=1.00)
    unit_price = models.DecimalField(max_digits=18, decimal_places=2)
    subtotal = models.DecimalField(max_digits=18, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    class Meta:
        abstract = True

class BaseBankAccount(BaseErpModel):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class BasePayment(BaseErpModel):
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    method = models.CharField(max_length=50)
    reference = models.CharField(max_length=100, blank=True)
    bank_fees = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    class Meta:
        abstract = True

class BasePaymentOrder(BaseErpModel):
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    concept = models.CharField(max_length=255)
    status = models.CharField(max_length=20)

    class Meta:
        abstract = True

class BaseWarehouse(BaseErpModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True

class BaseInventoryMovement(BaseErpModel):
    movement_type = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=18, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True

class BaseAuditTrail(BaseErpModel):
    action = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=50)
    entity_id = models.UUIDField()
    payload = models.JSONField()
    user_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    previous_hash = models.CharField(max_length=64, null=True, blank=True)
    integrity_hash = models.CharField(max_length=64)

    class Meta:
        abstract = True

# Compatibility Aliases for existing code
BaseAccount = LedgerAccount
BaseFiscalPeriod = FinancialPeriod
BaseAccountingTransaction = BaseJournalLine
BaseBankTransaction = BasePayment
