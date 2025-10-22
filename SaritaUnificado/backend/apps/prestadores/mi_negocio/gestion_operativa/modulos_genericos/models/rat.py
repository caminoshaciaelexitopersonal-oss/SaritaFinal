# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/models/rat.py
from django.db import models
from .base import Perfil

class RegistroActividadTuristica(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='registros_rat')
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"Registro RAT para {self.perfil.nombre_comercial} en {self.fecha}"
