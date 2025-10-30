# backend/apps/inventario/models.py
from django.db import models
from apps.prestadores.models import Perfil

class Producto(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='productos_inventario')
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
