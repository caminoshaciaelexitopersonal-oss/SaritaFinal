from django.db import models

class Valoracion(models.Model):
    puntuacion = models.IntegerField()
    comentario = models.TextField(blank=True)

    class Meta:
        app_label = 'admin_operativa'
