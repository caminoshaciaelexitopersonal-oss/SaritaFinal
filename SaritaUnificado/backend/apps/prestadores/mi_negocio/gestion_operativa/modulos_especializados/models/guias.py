# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/models/guias.py
from django.db import models
from ...modulos_genericos.models.base import Perfil
from django.core.exceptions import ValidationError

class Ruta(models.Model):
    DIFICULTAD_CHOICES = [
        ('facil', 'Fácil'),
        ('moderada', 'Moderada'),
        ('dificil', 'Difícil'),
        ('experto', 'Experto'),
    ]

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='rutas_turisticas')
    nombre = models.CharField(max_length=255)
    descripcion_corta = models.CharField(max_length=300)
    descripcion_larga = models.TextField()
    duracion_horas = models.DecimalField(max_digits=5, decimal_places=2, help_text="Duración estimada en horas.")
    distancia_km = models.DecimalField(max_digits=6, decimal_places=2, help_text="Distancia total en kilómetros.")
    dificultad = models.CharField(max_length=20, choices=DIFICULTAD_CHOICES, default='moderada')
    precio_persona = models.DecimalField(max_digits=10, decimal_places=2)
    punto_encuentro = models.CharField(max_length=255)
    foto_principal = models.ImageField(upload_to='rutas_turisticas/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.perfil.nombre_comercial}"

class HitoRuta(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name='hitos')
    nombre = models.CharField(max_length=200, help_text="Nombre del hito o parada (ej. 'Cascada La Chorrera')")
    descripcion = models.TextField(help_text="Descripción de lo que se hará o verá en este hito.")
    orden = models.PositiveIntegerField(help_text="Orden secuencial del hito en la ruta.")
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"{self.orden}. {self.nombre} (Ruta: {self.ruta.nombre})"

class Equipamiento(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='equipamientos')
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    cantidad_total = models.PositiveIntegerField()
    cantidad_disponible = models.PositiveIntegerField()
    foto = models.ImageField(upload_to='equipamiento_guias/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.cantidad_disponible}/{self.cantidad_total} disponibles)"

    def clean(self):
        if self.cantidad_disponible > self.cantidad_total:
            raise ValidationError('La cantidad disponible no puede ser mayor que la cantidad total.')
