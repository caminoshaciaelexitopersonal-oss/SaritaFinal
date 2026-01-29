from django.db import models

class TipoAlojamiento(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'

class Alojamiento(models.Model):
    tipo = models.ForeignKey(TipoAlojamiento, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=200)

    class Meta:
        app_label = 'admin_operativa'

class Habitacion(models.Model):
    alojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE, related_name='admin_habitaciones')
    numero = models.CharField(max_length=20)

    class Meta:
        app_label = 'admin_operativa'
