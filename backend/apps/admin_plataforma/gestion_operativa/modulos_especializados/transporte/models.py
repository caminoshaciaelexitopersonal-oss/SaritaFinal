from django.db import models
from ..modulos_genericos.perfil.models import TenantAwareModel

class Vehicle(TenantAwareModel):
    placa = models.CharField(max_length=20)
    modelo = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'
