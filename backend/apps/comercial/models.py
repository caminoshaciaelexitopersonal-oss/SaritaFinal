import uuid
from django.db import models

class Lead(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'New'
        QUALIFIED = 'qualified', 'Qualified'
        REJECTED = 'rejected', 'Rejected'
        CONVERTED = 'converted', 'Converted'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, blank=True)
    source = models.CharField(max_length=100, default='organic')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    score = models.IntegerField(default=0)
    estimated_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'comercial'

class Plan(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    monthly_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    storage_limit_gb = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'comercial'

class Opportunity(models.Model):
    class Stage(models.TextChoices):
        PROSPECTING = 'prospecting', 'Prospecting'
        WON = 'won', 'Won'
        LOST = 'lost', 'Lost'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='opportunities')
    stage = models.CharField(max_length=20, choices=Stage.choices, default=Stage.PROSPECTING)
    estimated_revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        app_label = 'comercial'

class Subscription(models.Model):
    class Status(models.TextChoices):
        TRIAL = 'TRIAL', 'Periodo de Prueba'
        ACTIVE = 'ACTIVE', 'Activa'
        SUSPENDED = 'SUSPENDED', 'Suspendida'
        CANCELED = 'CANCELED', 'Cancelada'

    class BillingCycle(models.TextChoices):
        MONTHLY = 'MONTHLY', 'Mensual'
        YEARLY = 'YEARLY', 'Anual'

    tenant_id = models.CharField(max_length=100, unique=True)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TRIAL)
    billing_cycle = models.CharField(max_length=20, choices=BillingCycle.choices, default=BillingCycle.MONTHLY)
    next_billing_date = models.DateField(null=True, blank=True)

    class Meta:
        app_label = 'comercial'

class PricingRule(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='pricing_rules')
    extra_gb_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        app_label = 'comercial'

class UsageMetric(models.Model):
    tenant_id = models.CharField(max_length=100)
    metric_type = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=15, decimal_places=4)
    period_start = models.DateField()
    period_end = models.DateField()

    class Meta:
        app_label = 'comercial'

class BillingCycle(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='billing_cycles')
    cycle_start = models.DateField()
    cycle_end = models.DateField()
    amount_calculated = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, default='pending')

    class Meta:
        app_label = 'comercial'
