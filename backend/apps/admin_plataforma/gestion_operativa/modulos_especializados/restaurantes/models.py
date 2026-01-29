from django.db import models
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel

class KitchenStation(TenantAwareModel):
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'

class RestaurantTable(TenantAwareModel):
    numero = models.CharField(max_length=20)
    capacidad = models.PositiveIntegerField(default=4)

    class Meta:
        app_label = 'admin_operativa'
