# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/models/crm.py
from django.db import models
from .base import Perfil

class Cliente(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='clientes')
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre
