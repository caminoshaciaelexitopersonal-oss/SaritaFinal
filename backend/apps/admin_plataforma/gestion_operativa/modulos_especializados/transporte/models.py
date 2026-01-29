from django.db import models
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel

class Vehicle(TenantAwareModel):
    placa = models.CharField(max_length=20)
    modelo = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'
