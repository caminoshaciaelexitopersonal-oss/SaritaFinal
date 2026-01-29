import uuid
from django.db import models
from django.conf import settings

class PerformanceMetric(models.Model):
    """
    Registra KPIs históricos para análisis de optimización.
    """
    class Domain(models.TextChoices):
        COMERCIAL = 'COMERCIAL', 'Comercial'
        CONTABLE = 'CONTABLE', 'Contable'
        FINANCIERO = 'FINANCIERO', 'Financiero'
        OPERATIVO = 'OPERATIVO', 'Operativo'
        ARCHIVISTICO = 'ARCHIVISTICO', 'Archivístico'
        GOBERNANZA = 'GOBERNANZA', 'Gobernanza'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    domain = models.CharField(max_length=50, choices=Domain.choices)
    metric_name = models.CharField(max_length=100) # ej: 'ROI', 'TrustLevel', 'ResolutionTime'
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['domain', 'metric_name']),
        ]

class OptimizationProposal(models.Model):
    """
    Recomendación del sistema para ajustar parámetros operativos o reglas.
    """
    class Status(models.TextChoices):
        PROPOSED = 'PROPOSED', 'Propuesta'
        APPROVED = 'APPROVED', 'Aprobada'
        REJECTED = 'REJECTED', 'Rechazada'
        EXECUTED = 'EXECUTED', 'Ejecutada'
        REVERTED = 'REVERTED', 'Revertida'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    domain = models.CharField(max_length=50, choices=PerformanceMetric.Domain.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PROPOSED)

    # --- Contenido de la Optimización ---
    hallazgo = models.TextField(help_text="Patrón detectado que justifica la optimización.")
    propuesta_ajuste = models.TextField(help_text="Descripción técnica del ajuste sugerido.")
    parametros_cambio = models.JSONField(help_text="Valores técnicos a modificar (ej: {'threshold': 0.85}).")
    impacto_esperado = models.TextField()

    # --- Control y Rollback ---
    config_previa = models.JSONField(help_text="Snapshot de la configuración antes del cambio.")
    decidida_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    justificacion_admin = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Propuesta de Optimización"
        verbose_name_plural = "Propuestas de Optimización"

class OptimizationAuditLog(models.Model):
    """
    Log especializado de gobernanza para la Fase 6.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    proposal = models.ForeignKey(OptimizationProposal, on_delete=models.CASCADE, related_name="audit_logs")
    accion = models.CharField(max_length=50) # ej: 'APPROVE', 'EXECUTE', 'ROLLBACK'
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    detalles = models.JSONField(default=dict)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
