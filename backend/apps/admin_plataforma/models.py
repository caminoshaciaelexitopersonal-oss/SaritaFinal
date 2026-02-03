
import uuid
from django.db import models
from django.conf import settings
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class Plan(models.Model):
    """
    Define un plan de suscripción que la plataforma Sarita puede vender.
    """
    class TipoUsuario(models.TextChoices):
        GOBIERNO = 'GOBIERNO', 'Gobierno'
        PRESTADOR = 'PRESTADOR', 'Prestador'

    class Frecuencia(models.TextChoices):
        MENSUAL = 'MENSUAL', 'Mensual'
        SEMESTRAL = 'SEMESTRAL', 'Semestral'
        ANUAL = 'ANUAL', 'Anual'

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(default="")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    frecuencia = models.CharField(max_length=20, choices=Frecuencia.choices, default=Frecuencia.MENSUAL)
    tipo_usuario_objetivo = models.CharField(max_length=20, choices=TipoUsuario.choices, default=TipoUsuario.PRESTADOR)
    is_active = models.BooleanField(default=True, help_text="Indica si el plan está disponible para nuevas suscripciones.")

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        app_label = 'admin_plataforma'

class GovernanceAuditLog(models.Model):
    """
    Registro unificado de auditoría para el núcleo de gobernanza.
    Almacena cada intención procesada por el kernel.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="governance_logs"
    )
    intencion = models.CharField(max_length=255, db_index=True)
    parametros = models.JSONField(default=dict)
    resultado = models.JSONField(default=dict)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    success = models.BooleanField(default=True)
    error_message = models.TextField(null=True, blank=True)
    es_intervencion_soberana = models.BooleanField(default=False)

    # --- Hardening Técnico (RC-S): Integridad de Auditoría ---
    integrity_hash = models.CharField(max_length=64, null=True, blank=True, db_index=True)
    previous_hash = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        app_label = 'admin_plataforma'
        ordering = ['-timestamp']

class GovernancePolicy(models.Model):
    """
    Define reglas globales de gobernanza que condicionan la operación del sistema.
    Permite al Super Admin establecer bloqueos, umbrales y requisitos transversales.
    """
    TYPE_CHOICES = [
        ('BLOCK', 'Bloqueo Total'),
        ('THRESHOLD', 'Umbral de Alerta/Bloqueo'),
        ('REQUIRE_VERIFICATION', 'Requiere Verificación Manual'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    domain = models.CharField(max_length=100, default='global', help_text="Dominio afectado (global, comercial, etc.)")
    affected_intentions = models.JSONField(default=list, help_text="Lista de intenciones que responden a esta política.")
    config = models.JSONField(default=dict, help_text="Configuración dinámica (ej: {'limit': 1000})")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'admin_plataforma'
        verbose_name = "Política de Gobernanza"
        verbose_name_plural = "Políticas de Gobernanza"

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

class Suscripcion(models.Model):
    """
    Representa la suscripción de un cliente a un plan específico.
    """
    cliente = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="admin_suscripciones"
    )
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name="admin_suscripciones")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    is_active = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'admin_plataforma'
