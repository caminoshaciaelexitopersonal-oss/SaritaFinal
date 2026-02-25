from django.db import models
from apps.core_erp.base_models import BaseErpModel

class Jurisdiction(BaseErpModel):
    """
    Representa una jurisdicción fiscal (País/Estado).
    """
    country_code = models.CharField(max_length=2, unique=True) # ISO 3166-1 alpha-2
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=3)
    tax_framework = models.CharField(max_length=50, default='STANDARD')
    accounting_standard = models.CharField(max_length=20, default='IFRS')
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'core_erp'
        verbose_name = "Jurisdiction"

    def __str__(self):
        return f"{self.name} ({self.country_code})"

class TaxRule(BaseErpModel):
    """
    Reglas fiscales versionables por jurisdicción.
    """
    class TaxType(models.TextChoices):
        VAT = 'VAT', 'Value Added Tax'
        GST = 'GST', 'Goods and Services Tax'
        WITHHOLDING = 'WITHHOLDING', 'Withholding Tax'
        CORPORATE = 'CORPORATE', 'Corporate Income Tax'
        HOTEL = 'HOTEL', 'Hotel/Tourism Tax'

    jurisdiction = models.ForeignKey(Jurisdiction, on_delete=models.CASCADE, related_name='rules')
    tax_type = models.CharField(max_length=20, choices=TaxType.choices)
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=5, decimal_places=4)
    version = models.CharField(max_length=10, default='1.0')
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)
    legal_reference = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'core_erp'
        verbose_name = "Tax Rule"

class RegulatoryCalendar(BaseErpModel):
    """
    Calendario regulatorio para cumplimiento automático.
    """
    jurisdiction = models.ForeignKey(Jurisdiction, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    deadline_day = models.IntegerField(help_text="Día del mes o relativo")
    frequency = models.CharField(max_length=20, default='MONTHLY')
    responsible_role = models.CharField(max_length=100, default='TAX_OFFICER')

    class Meta:
        app_label = 'core_erp'
        verbose_name = "Regulatory Calendar"

class TaxAuditTrail(BaseErpModel):
    """
    Trazabilidad total de cálculos fiscales.
    """
    transaction_reference = models.CharField(max_length=100)
    jurisdiction = models.ForeignKey(Jurisdiction, on_delete=models.SET_NULL, null=True)
    rule_applied = models.ForeignKey(TaxRule, on_delete=models.SET_NULL, null=True)
    base_amount = models.DecimalField(max_digits=18, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=18, decimal_places=2)
    calculation_path = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'core_erp'
