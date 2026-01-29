from django.db import models

class VehiculoDeAlquiler(models.Model):
    nombre = models.CharField(max_length=200)
    placa = models.CharField(max_length=20)

    class Meta:
        app_label = 'admin_operativa'

class Alquiler(models.Model):
    vehiculo = models.ForeignKey(VehiculoDeAlquiler, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()

    class Meta:
        app_label = 'admin_operativa'
