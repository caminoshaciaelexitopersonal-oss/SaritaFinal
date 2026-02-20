from django.db import models
from apps.core_erp.base.base_models import BaseInvoice

class Invoice(BaseInvoice):
    client_id = models.UUIDField() # ID de la empresa (Company)
    total_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        app_label = 'core_erp_billing'

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=18, decimal_places=2, default=1)
    unit_price = models.DecimalField(max_digits=18, decimal_places=2)
    subtotal = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        app_label = 'core_erp_billing'
