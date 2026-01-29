from django.db import models
from ..perfil.models import TenantAwareModel

class InventoryItem(TenantAwareModel):
    nombre = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)

    class Meta:
        app_label = 'admin_operativa'
