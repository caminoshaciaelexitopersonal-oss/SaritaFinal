from django.db import models
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel

class Skill(TenantAwareModel):
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'

class TourDetail(models.Model):
    # Relacionado con un producto que actúa como tour
    nombre_guia = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'
