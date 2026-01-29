from django.db import models

class OrganizadorEvento(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        app_label = 'admin_operativa'

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField()
    organizador = models.ForeignKey(OrganizadorEvento, on_delete=models.CASCADE, related_name='admin_eventos')

    class Meta:
        app_label = 'admin_operativa'
