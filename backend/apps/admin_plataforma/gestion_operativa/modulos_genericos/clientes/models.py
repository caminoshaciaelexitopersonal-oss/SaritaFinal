# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/clientes/models.py
from django.db import models
from ..perfil.models import ProviderProfile

class Cliente(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='clientes')
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre
