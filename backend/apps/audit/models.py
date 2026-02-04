from django.db import models
import uuid

class AuditLog(models.Model):
    class Action(models.TextChoices):
        USER_LOGIN_SUCCESS = 'USER_LOGIN_SUCCESS', 'Inicio de sesión exitoso'
        USER_LOGIN_FAILED = 'USER_LOGIN_FAILED', 'Intento de inicio de sesión fallido'
        DOCUMENT_CREATED = 'DOCUMENT_CREATED', 'Creó concepto de documento'
        VERSION_UPLOADED = 'VERSION_UPLOADED', 'Subió nueva versión'
        VERSION_DOWNLOADED = 'VERSION_DOWNLOADED', 'Descargó versión'
        VERSION_DELETED = 'VERSION_DELETED', 'Eliminó versión'
        VERSION_VERIFIED = 'VERSION_VERIFIED', 'Verificó integridad de versión'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('api.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=150)
    company = models.ForeignKey('companies.Company', on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=50, choices=Action.choices, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    details = models.JSONField(default=dict)

    class Meta:
        verbose_name = "Audit Log Entry"
        verbose_name_plural = "Audit Log"
        ordering = ['-timestamp']

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.username} -> {self.get_action_display()}"


class ForensicSecurityLog(models.Model):
    """
    Registro forense de alta fidelidad para la contención de ataques (S-0.3).
    Almacena trazas técnicas de actividad sospechosa detectada por el sistema de defensa.
    """
    class ThreatLevel(models.TextChoices):
        LOW = 'LOW', 'Baja'
        MEDIUM = 'MEDIUM', 'Media'
        HIGH = 'HIGH', 'Alta'
        CRITICAL = 'CRITICAL', 'Crítica (Amenaza Activa)'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    source_ip = models.GenericIPAddressField(null=True, blank=True)
    user = models.ForeignKey('api.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    threat_level = models.CharField(max_length=20, choices=ThreatLevel.choices, default=ThreatLevel.LOW)
    attack_vector = models.CharField(max_length=100, help_text="Ej: XSS_ATTEMPT, BRUTE_FORCE, GOVERNANCE_BYPASS")
    payload_captured = models.JSONField(help_text="Cuerpo de la petición o parámetros sospechosos.")
    headers_captured = models.JSONField(help_text="Headers HTTP de la petición maliciosa.")
    action_taken = models.CharField(max_length=255, help_text="Ej: SESSION_QUARANTINE, TOKEN_INVALIDATED")
    integrity_hash = models.CharField(max_length=64, null=True, blank=True, help_text="Hash SHA-256 para prevenir alteración forense.")

    class Meta:
        verbose_name = "Forensic Security Log"
        verbose_name_plural = "Forensic Security Logs"
        ordering = ['-timestamp']

    def __str__(self):
        return f"[{self.threat_level}] {self.attack_vector} @ {self.timestamp}"
