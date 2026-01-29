from django.db import models
from ..perfil.models import TenantAwareModel

class PoliticaCancelacion(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'

class Reserva(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='PENDIENTE')

    class Meta:
        app_label = 'admin_operativa'

class ReservaServicioAdicional(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='admin_servicios_adicionales')
    nombre_servicio = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'
