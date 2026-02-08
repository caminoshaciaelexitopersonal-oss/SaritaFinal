from django.db import models
import uuid
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel

class TaxConfiguration(TenantAwareModel):
    """
    Configuración configurable de impuestos (IVA, Retenciones).
    """
    class TaxType(models.TextChoices):
        IVA = 'IVA', 'IVA (Impuesto al Valor Agregado)'
        RETEFUENTE = 'RETEFUENTE', 'Retención en la Fuente'
        ICA = 'ICA', 'Impuesto de Industria y Comercio'

    name = models.CharField(max_length=100)
    tax_type = models.CharField(max_length=20, choices=TaxType.choices)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=True)

    # Cuentas contables asociadas para automatización
    cuenta_debito_ref_id = models.UUIDField(null=True, blank=True)
    cuenta_credito_ref_id = models.UUIDField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"

    class Meta: app_label = 'prestadores'
