from django.db import models

class Horario(models.Model):
    dia_semana = models.IntegerField()
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()

    class Meta:
        app_label = 'admin_operativa'

class ExcepcionHorario(models.Model):
    fecha = models.DateField()
    cerrado = models.BooleanField(default=True)

    class Meta:
        app_label = 'admin_operativa'
