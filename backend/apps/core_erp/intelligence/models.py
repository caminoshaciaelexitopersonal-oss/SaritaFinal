from django.db import models
from apps.core_erp.base_models import BaseErpModel

class FinancialProjection(BaseErpModel):
    """
    Predicciones de flujo de caja y obligaciones fiscales.
    """
    class ProjectionType(models.TextChoices):
        CASH_FLOW = 'CASH_FLOW', 'Cash Flow Forecast'
        TAX_LIABILITY = 'TAX_LIABILITY', 'Tax Liability Projection'
        REVENUE = 'REVENUE', 'Revenue Prediction'

    tenant = models.ForeignKey('core_erp.Tenant', on_delete=models.CASCADE)
    projection_type = models.CharField(max_length=20, choices=ProjectionType.choices)
    target_date = models.DateField()
    estimated_amount = models.DecimalField(max_digits=18, decimal_places=2)
    confidence_score = models.DecimalField(max_digits=3, decimal_places=2, help_text="0.00 to 1.00")
    model_version = models.CharField(max_length=50)
    parameters_used = models.JSONField()

    class Meta:
        app_label = 'core_erp'

class StrategicScenario(BaseErpModel):
    """
    Motor de Simulación Estratégica.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    base_snapshot_date = models.DateField()
    variables = models.JSONField(help_text="Parámetros de simulación (e.g. nuevo impuesto, cambio FX)")
    simulated_kpis = models.JSONField(null=True)
    created_by = models.CharField(max_length=100)

    class Meta:
        app_label = 'core_erp'
