import uuid
from django.db import models

class Plan(models.Model):
    class BillingType(models.TextChoices):
        FLAT = 'flat', 'Flat Rate'
        USAGE = 'usage', 'Usage Based'
        HYBRID = 'hybrid', 'Hybrid'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    monthly_price = models.DecimalField(max_digits=12, decimal_places=2)
    annual_price = models.DecimalField(max_digits=12, decimal_places=2)
    included_usage = models.JSONField(default=dict, help_text="Ej: {'api_calls': 1000}")
    overage_price = models.JSONField(default=dict, help_text="Ej: {'api_calls': 0.01}")
    billing_type = models.CharField(
        max_length=20,
        choices=BillingType.choices,
        default=BillingType.FLAT
    )
    trial_days = models.IntegerField(default=14)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'commercial_engine'
