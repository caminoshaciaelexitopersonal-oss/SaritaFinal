# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/models/reportes.py
from django.db import models
from .base import Perfil

class Reporte(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='reportes')
    nombre_reporte = models.CharField(max_length=255)
    datos = models.JSONField()

    def __str__(self):
        return self.nombre_reporte
