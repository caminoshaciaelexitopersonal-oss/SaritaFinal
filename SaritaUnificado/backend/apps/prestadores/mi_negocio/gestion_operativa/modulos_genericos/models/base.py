# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/models/base.py
from django.db import models
from django.conf import settings

from django.utils.text import slugify

from ..perfil import Perfil, CategoriaPrestador


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
