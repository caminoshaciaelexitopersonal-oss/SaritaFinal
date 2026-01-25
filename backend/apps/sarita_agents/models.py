# backend/apps/sarita_agents/models.py
import uuid
from django.db import models

class Mision(models.Model):
    """
    Registro de más alto nivel. Representa la directiva original del General.
    Es el ancla para toda la trazabilidad.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    directiva_original = models.JSONField(help_text="La directiva JSON original recibida por el orquestador.")
    dominio = models.CharField(max_length=100, help_text="Dominio de negocio objetivo (ej. 'prestadores').")
    estado = models.CharField(max_length=50, default='PENDIENTE', choices=[
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROGRESO', 'En Progreso'),
        ('COMPLETADA', 'Completada'),
        ('FALLIDA', 'Fallida'),
    ])
    resultado_final = models.JSONField(null=True, blank=True, help_text="El informe final consolidado de la misión.")
    timestamp_inicio = models.DateTimeField(auto_now_add=True)
    timestamp_fin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Misión {self.id} ({self.dominio}) - {self.estado}"

class PlanTáctico(models.Model):
    """
    El plan detallado generado por un Capitán para cumplir una misión.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mision = models.ForeignKey(Mision, on_delete=models.CASCADE, related_name='planes_tacticos')
    capitan_responsable = models.CharField(max_length=255, help_text="Clase del Capitán que generó el plan.")
    pasos_del_plan = models.JSONField(help_text="Los pasos estructurados del plan.")
    estado = models.CharField(max_length=50, default='PLANIFICADO', choices=[
        ('PLANIFICADO', 'Planificado'),
        ('EN_EJECUCION', 'En Ejecución'),
        ('COMPLETADO', 'Completado'),
        ('FALLIDO', 'Fallido'),
    ])
    timestamp_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plan {self.id} para Misión {self.mision_id}"

class TareaDelegada(models.Model):
    """
    Una tarea atómica individual delegada a un Teniente.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plan_tactico = models.ForeignKey(PlanTáctico, on_delete=models.CASCADE, related_name='tareas')
    teniente_asignado = models.CharField(max_length=255, help_text="Identificador del Teniente responsable.")
    descripcion_tarea = models.TextField()
    parametros = models.JSONField(default=dict)
    estado = models.CharField(max_length=50, default='PENDIENTE', choices=[
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROGRESO', 'En Progreso'),
        ('COMPLETADA', 'Completada'),
        ('FALLIDA', 'Fallida'),
    ])
    timestamp_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tarea {self.id} ({self.estado})"

class RegistroDeEjecucion(models.Model):
    """
    Un log detallado de un intento de ejecución de una TareaDelegada.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tarea_delegada = models.ForeignKey(TareaDelegada, on_delete=models.CASCADE, related_name='logs_ejecucion')
    timestamp = models.DateTimeField(auto_now_add=True)
    exitoso = models.BooleanField()
    salida_log = models.TextField(null=True, blank=True, help_text="Salida estándar o log de la ejecución.")
    resultado = models.JSONField(null=True, blank=True, help_text="El resultado estructurado de la ejecución.")

    def __str__(self):
        return f"Log de Tarea {self.tarea_delegada_id} @ {self.timestamp}"
