from django.db import models
from apps.core_erp.base_models import BaseErpModel

class Tenant(BaseErpModel):
    """
    Entidad fundamental de aislamiento. Representa una empresa o prestador.
    """
    name = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255, blank=True)
    tax_id = models.CharField(max_length=50, unique=True)
    currency = models.CharField(max_length=3, default='COP')
    is_active = models.BooleanField(default=True)

    # Soporte opcional para jerarquía Holding
    parent_company = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subsidiaries'
    )

    class Meta:
        app_label = 'core_erp'
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"

    def __str__(self):
        return f"{self.name} ({self.tax_id})"
