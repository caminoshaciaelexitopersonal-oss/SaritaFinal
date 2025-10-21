# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/models/configuracion.py
from django.db import models
from .base import Perfil

class ConfiguracionPrestador(models.Model):
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name='configuracion')
    recibir_notificaciones = models.BooleanField(default=True)

    def __str__(self):
        return f"Configuración para {self.perfil.nombre_comercial}"
