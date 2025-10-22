# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/models/hoteles.py
from django.db import models
from ...modulos_genericos.models.base import Perfil

class Habitacion(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='habitaciones')
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class ServicioAdicionalHotel(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='servicios_adicionales_hotel')
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
