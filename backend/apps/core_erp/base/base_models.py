from django.db import models
import uuid

class BaseErpModel(models.Model):
    """
    Modelo base para todas las entidades del Core ERP.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class BasePaymentOrder(BaseErpModel):
    """
    Abstracción de una orden de pago.
    """
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    concept = models.CharField(max_length=255)
    status = models.CharField(max_length=20)

    class Meta:
        abstract = True

class BaseBankTransaction(BaseErpModel):
    """
    Abstracción de una transacción bancaria.
    """
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)

    class Meta:
        abstract = True

class BaseInventoryMovement(BaseErpModel):
    """
    Abstracción de un movimiento de stock.
    """
    movement_type = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=18, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True

class BaseWarehouse(BaseErpModel):
    """
    Abstracción de un almacén o bodega.
    """
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True

class BaseBankAccount(BaseErpModel):
    """
    Abstracción de una cuenta bancaria.
    """
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class BaseAccount(BaseErpModel):
    """
    Abstracción de una cuenta contable (Paso 2).
    """
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class BaseJournalEntry(BaseErpModel):
    """
    Abstracción de un asiento contable (Paso 2).
    """
    date = models.DateField()
    reference = models.CharField(max_length=255)
    description = models.TextField()
    is_posted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class BaseAccountingTransaction(BaseErpModel):
    """
    Abstracción de un movimiento de débito/crédito.
    """
    debit = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    credit = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    class Meta:
        abstract = True

class BaseInvoice(BaseErpModel):
    """
    Abstracción de una factura (Paso 2).
    """
    number = models.CharField(max_length=50)
    issue_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=30)

    class Meta:
        abstract = True

class BaseFiscalPeriod(BaseErpModel):
    """
    Abstracción de un periodo contable/fiscal.
    """
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_closed = models.BooleanField(default=False)

    class Meta:
        abstract = True
