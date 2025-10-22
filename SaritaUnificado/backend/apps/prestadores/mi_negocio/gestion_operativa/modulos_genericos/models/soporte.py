# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/models/soporte.py
from django.db import models
from .base import Perfil

class TicketSoporte(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='tickets_soporte')
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()
    resuelto = models.BooleanField(default=False)

    def __str__(self):
        return self.asunto
