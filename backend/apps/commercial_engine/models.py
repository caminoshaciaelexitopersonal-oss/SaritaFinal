from .plan_model import SaaSPlan
from .lead_model import SaaSLead
import uuid
from django.db import models

class SaaSSubscription(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Activa'
        PAST_DUE = 'PAST_DUE', 'Mora'
        CANCELED = 'CANCELED', 'Cancelada'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant_id = models.CharField(max_length=100, unique=True)
    plan = models.ForeignKey(SaaSPlan, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

    start_date = models.DateField(auto_now_add=True)
    next_billing_date = models.DateField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tenant_id} - {self.plan.name}"

class UsageEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant_id = models.CharField(max_length=100, db_index=True)
    metric_type = models.CharField(max_length=50, db_index=True)
    quantity = models.DecimalField(max_digits=15, decimal_places=4)
    timestamp = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(default=dict, blank=True)

class UsageAggregation(models.Model):
    subscription = models.ForeignKey(SaaSSubscription, on_delete=models.CASCADE)
    metric_type = models.CharField(max_length=50)
    total_quantity = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    period_start = models.DateField()
    period_end = models.DateField()
    is_billed = models.BooleanField(default=False)
