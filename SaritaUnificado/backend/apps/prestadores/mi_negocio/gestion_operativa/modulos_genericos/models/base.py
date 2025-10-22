# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/models/base.py
from django.db import models
from django.conf import settings

from django.utils.text import slugify

class CategoriaPrestador(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Activo', 'Activo'),
        ('Rechazado', 'Rechazado'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil_prestador')
    nombre_comercial = models.CharField(max_length=255)
    categoria = models.ForeignKey(CategoriaPrestador, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Pendiente')

    # Campos de puntuación
    puntuacion_total = models.IntegerField(default=0)
    puntuacion_capacitacion = models.IntegerField(default=0)
    puntuacion_reseñas = models.IntegerField(default=0)
    puntuacion_verificacion = models.IntegerField(default=0)
    puntuacion_formularios = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre_comercial

    def recalcular_puntuacion_total(self):
        self.puntuacion_total = (
            self.puntuacion_capacitacion +
            self.puntuacion_reseñas +
            self.puntuacion_verificacion +
            self.puntuacion_formularios
        )
        self.save(update_fields=['puntuacion_total'])

class Puntuacion(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='puntuaciones')
    puntuacion = models.IntegerField()

class Verificacion(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='verificaciones')
    verificado = models.BooleanField(default=False)

class Checklist(models.Model):
    nombre = models.CharField(max_length=100)

class ItemChecklist(models.Model):
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name='items')
    texto = models.CharField(max_length=255)

class FormularioDinamico(models.Model):
    nombre = models.CharField(max_length=100)

class CampoFormulario(models.Model):
    formulario = models.ForeignKey(FormularioDinamico, on_delete=models.CASCADE, related_name='campos')
    etiqueta = models.CharField(max_length=100)
    tipo_campo = models.CharField(max_length=50)

class RespuestaFormulario(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='respuestas')
    campo = models.ForeignKey(CampoFormulario, on_delete=models.CASCADE)
    valor = models.TextField()
