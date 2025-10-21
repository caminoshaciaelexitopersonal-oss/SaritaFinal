# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/models/contabilidad.py
from django.db import models
from .base import Perfil

class Costo(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='costos')
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descripcion

class Inventario(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='inventario')
    nombre_item = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_item
