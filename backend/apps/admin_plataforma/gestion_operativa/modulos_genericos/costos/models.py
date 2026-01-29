from django.db import models
from ..perfil.models import TenantAwareModel

class Costo(TenantAwareModel):
    nombre = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        app_label = 'admin_operativa'
