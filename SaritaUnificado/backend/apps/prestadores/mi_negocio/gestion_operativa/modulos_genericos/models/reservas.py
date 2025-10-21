# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/models/reservas.py
from django.db import models
from .base import Perfil

class Reserva(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    nombre_cliente = models.CharField(max_length=255)

    def __str__(self):
        return f"Reserva para {self.nombre_cliente}"
