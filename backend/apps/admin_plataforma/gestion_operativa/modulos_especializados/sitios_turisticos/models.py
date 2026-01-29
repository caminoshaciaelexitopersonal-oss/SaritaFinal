from django.db import models

class SitioTuristico(models.Model):
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=255)

    class Meta:
        app_label = 'admin_operativa'

class ActividadEnSitio(models.Model):
    sitio = models.ForeignKey(SitioTuristico, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'
