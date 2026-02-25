from django.db import models
from apps.core_erp.base_models import BaseErpModel

class HoldingEntity(BaseErpModel):
    """
    Representa la matriz o entidad holding que consolida.
    """
    name = models.CharField(max_length=255)
    base_currency = models.CharField(max_length=3, default='COP')
    reporting_standard = models.CharField(max_length=50, default='IFRS')

    class Meta:
        app_label = 'core_erp'
        verbose_name = "Holding Entity"
        verbose_name_plural = "Holding Entities"

    def __str__(self):
        return self.name

class HoldingMembership(BaseErpModel):
    """
    Define la relación entre un Holding y un Tenant.
    """
    class ConsolidationMethod(models.TextChoices):
        FULL = 'FULL', 'Full Consolidation'
        EQUITY = 'EQUITY', 'Equity Method'
        PROPORTIONAL = 'PROPORTIONAL', 'Proportional Consolidation'

    holding = models.ForeignKey(HoldingEntity, on_delete=models.CASCADE, related_name='memberships')
    tenant = models.ForeignKey('core_erp.Tenant', on_delete=models.CASCADE, related_name='holding_memberships')
    ownership_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)
    consolidation_method = models.CharField(
        max_length=20,
        choices=ConsolidationMethod.choices,
        default=ConsolidationMethod.FULL
    )

    class Meta:
        app_label = 'core_erp'
        unique_together = ('holding', 'tenant')

class IntercompanyAccountMapping(BaseErpModel):
    """
    Mapea cuentas que deben eliminarse en el proceso de consolidación.
    """
    holding = models.ForeignKey(HoldingEntity, on_delete=models.CASCADE, related_name='intercompany_mappings')
    account_code_prefix = models.CharField(max_length=20, blank=True, null=True)
    account_name_pattern = models.CharField(max_length=255, help_text="Patrón para eliminación")
    description = models.TextField(blank=True)

    class Meta:
        app_label = 'core_erp'

class ConsolidatedReportSnapshot(BaseErpModel):
    """
    Audit trail for consolidated financial reports.
    """
    holding = models.ForeignKey(HoldingEntity, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=50)
    period = models.CharField(max_length=20)
    generated_at = models.DateTimeField(auto_now_add=True)
    fx_rates_used = models.JSONField()
    tenants_included = models.JSONField()
    data = models.JSONField()
    method_applied = models.CharField(max_length=50)
    correlation_id = models.CharField(max_length=100, db_index=True, null=True, blank=True)

    class Meta:
        app_label = 'core_erp'
