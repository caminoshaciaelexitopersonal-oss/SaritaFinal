from django.db import models
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel

class Amenity(TenantAwareModel):
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'

class RoomType(TenantAwareModel):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    class Meta:
        app_label = 'admin_operativa'

class Room(TenantAwareModel):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='admin_rooms')
    numero = models.CharField(max_length=20)

    class Meta:
        app_label = 'admin_operativa'
