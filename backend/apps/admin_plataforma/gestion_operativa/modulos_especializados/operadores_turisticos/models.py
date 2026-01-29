from django.db import models

class OperadorTuristico(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        app_label = 'admin_operativa'

class PaqueteTuristico(models.Model):
    operador = models.ForeignKey(OperadorTuristico, on_delete=models.CASCADE, related_name='admin_paquetes')
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        app_label = 'admin_operativa'

class ItinerarioDia(models.Model):
    paquete = models.ForeignKey(PaqueteTuristico, on_delete=models.CASCADE, related_name='admin_itinerarios')
    dia = models.IntegerField()
    actividad = models.TextField()

    class Meta:
        app_label = 'admin_operativa'
