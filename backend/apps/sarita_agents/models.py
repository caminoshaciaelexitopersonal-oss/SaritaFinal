# backend/apps/sarita_agents/models.py
import uuid
from django.db import models

class Mision(models.Model):
    """
    Registro de más alto nivel. Representa la directiva original del General.

    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idempotency_key = models.UUIDField(unique=True, null=True, blank=True, help_text="Clave única para prevenir duplicados.")

    directiva_original = models.JSONField(help_text="La directiva JSON original recibida por el orquestador.")
    dominio = models.CharField(max_length=100, help_text="Dominio de negocio objetivo (ej. 'prestadores').")
    estado = models.CharField(max_length=50, default='PENDIENTE', choices=[
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROGRESO', 'En Progreso'),
        ('COMPLETADA', 'Completada'),
        ('FALLIDA', 'Fallida'),

        ('COMPLETADA_PARCIALMENTE', 'Completada Parcialmente'),

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

        ('COMPLETADO_PARCIALMENTE', 'Completado Parcialmente'),

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

        ('EN_COLA', 'En Cola'),
        ('EN_PROGRESO', 'En Progreso'),
        ('REINTENTANDO', 'Reintentando'),

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

# --- Jerarquía Reforzada Fase 1: Sargentos y Soldados ---

class Sargento(models.Model):
    """
    Ejecutor atómico IA.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_identificador = models.CharField(max_length=255, unique=True, help_text="Ej: sargento_validacion_precio")
    dominio = models.CharField(max_length=100)
    funcion_principal = models.TextField()

    def __str__(self):
        return f"Sargento {self.nombre_identificador}"

class Soldado(models.Model):
    """
    Ejecutor humano bajo gobernanza del sistema.
    Cada Sargento tiene exactamente 5 soldados.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sargento = models.ForeignKey(Sargento, on_delete=models.CASCADE, related_name='soldados')
    usuario_asignado = models.ForeignKey('api.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    posicion = models.PositiveSmallIntegerField(help_text="Posición del 1 al 5 en el escuadrón.")
    esta_disponible = models.BooleanField(default=True)

    class Meta:
        unique_together = ('sargento', 'posicion')
        constraints = [
            models.CheckConstraint(check=models.Q(posicion__gte=1, posicion__lte=5), name='posicion_soldado_1_a_5')
        ]

    def __str__(self):
        return f"Soldado {self.posicion} de {self.sargento.nombre_identificador}"

class OrdenManual(models.Model):
    """
    Órdenes emitidas por un Sargento para ser ejecutadas por un Soldado (Humano).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sargento = models.ForeignKey(Sargento, on_delete=models.CASCADE)
    soldado = models.ForeignKey(Soldado, on_delete=models.CASCADE, related_name='ordenes')
    descripcion = models.TextField()
    evidencia_requerida = models.TextField()
    parametros = models.JSONField(default=dict)
    estado = models.CharField(max_length=20, default='PENDIENTE', choices=[
        ('PENDIENTE', 'Pendiente'),
        ('EN_EJECUCION', 'En Ejecución'),
        ('VALIDANDO', 'Validando Evidencia'),
        ('COMPLETADA', 'Completada'),
        ('RECHAZADA', 'Rechazada'),
    ])
    evidencia_url = models.URLField(null=True, blank=True)
    bitacora_ejecucion = models.TextField(blank=True)
    timestamp_creacion = models.DateTimeField(auto_now_add=True)
    timestamp_finalizacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Orden {self.id} -> Soldado {self.soldado.posicion}"
 

# --- Modelos de Dominio (Ejemplo para Fase U) ---

class Prestador(models.Model):
    """
    Modelo simple para representar a un Prestador de Servicios Turísticos.
    Creado para la prueba de concepto de la Fase U.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    activo = models.BooleanField(default=False)
    timestamp_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.email})"
