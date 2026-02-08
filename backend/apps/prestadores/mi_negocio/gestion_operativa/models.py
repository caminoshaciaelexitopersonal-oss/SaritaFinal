from django.db import models
import uuid
from django.utils import timezone
from .modulos_genericos.perfil.models import TenantAwareModel

class ProcesoOperativo(TenantAwareModel):
    """
    Representa una orquestación de tareas para cumplir un objetivo.
    """
    class EstadoProceso(models.TextChoices):
        PLANIFICADO = 'PLANIFICADO', 'Planificado'
        EN_EJECUCION = 'EN_EJECUCION', 'En Ejecución'
        COMPLETADO = 'COMPLETADO', 'Completado'
        FALLIDO = 'FALLIDO', 'Fallido'
        SUSPENDIDO = 'SUSPENDIDO', 'Suspendido'

    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=EstadoProceso.choices, default=EstadoProceso.PLANIFICADO)
    inicio_real = models.DateTimeField(null=True, blank=True)
    fin_real = models.DateTimeField(null=True, blank=True)

    class Meta: app_label = 'prestadores'

class TareaOperativa(TenantAwareModel):
    """
    Una unidad mínima de trabajo dentro de un proceso.
    """
    proceso = models.ForeignKey(ProcesoOperativo, on_delete=models.CASCADE, related_name='tareas')
    nombre = models.CharField(max_length=255)
    responsable_id = models.UUIDField(null=True, blank=True)
    estado = models.CharField(max_length=20, default='PENDIENTE')
    fecha_limite = models.DateTimeField()

    class Meta: app_label = 'prestadores'
