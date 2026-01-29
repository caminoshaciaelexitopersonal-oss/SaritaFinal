from django.db import models

class CompaniaTransporte(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        app_label = 'admin_operativa'

class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'

class Vehiculo(models.Model):
    compania = models.ForeignKey(CompaniaTransporte, on_delete=models.CASCADE, related_name='admin_vehiculos')
    tipo = models.ForeignKey(TipoVehiculo, on_delete=models.PROTECT)
    placa = models.CharField(max_length=20)

    class Meta:
        app_label = 'admin_operativa'

class Ruta(models.Model):
    nombre = models.CharField(max_length=200)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'
