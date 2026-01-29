from django.db import models

class PaqueteTuristico(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        app_label = 'admin_operativa'

class ReservaPaquete(models.Model):
    paquete = models.ForeignKey(PaqueteTuristico, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'admin_operativa'
