from django.db import models
import uuid
import hashlib
import json
from django.utils import timezone

class AuditLog(models.Model):
    class Action(models.TextChoices):
        USER_LOGIN_SUCCESS = 'USER_LOGIN_SUCCESS', 'Inicio de sesión exitoso'
        USER_LOGIN_FAILED = 'USER_LOGIN_FAILED', 'Intento de inicio de sesión fallido'
        DOCUMENT_CREATED = 'DOCUMENT_CREATED', 'Creó concepto de documento'
        VERSION_UPLOADED = 'VERSION_UPLOADED', 'Subió nueva versión'
        VERSION_DOWNLOADED = 'VERSION_DOWNLOADED', 'Descargó versión'
        VERSION_DELETED = 'VERSION_DELETED', 'Eliminó versión'
        VERSION_VERIFIED = 'VERSION_VERIFIED', 'Verificó integridad de versión'
        # --- ACCIONES COMERCIALES ---
        SALE_CREATED = 'SALE_CREATED', 'Operación comercial iniciada'
        SALE_CONFIRMED = 'SALE_CONFIRMED', 'Operación comercial confirmada'
        INVOICE_GENERATED = 'INVOICE_GENERATED', 'Factura de venta generada'

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
    previous_hash = models.CharField(max_length=64, null=True, blank=True, help_text="Hash de la entrada anterior para asegurar la integridad de la cadena.")
    integrity_hash = models.CharField(max_length=64, null=True, blank=True, help_text="Hash SHA-256 para prevenir alteración forense.")

    @classmethod
    def log_event(cls, threat_level, attack_vector, payload_captured, headers_captured, action_taken, user=None, source_ip=None):
        # Generar timestamp fijo para asegurar reproducibilidad del hash
        current_time = timezone.now()

        last_entry = cls.objects.order_by('-timestamp').first()
        prev_hash = last_entry.integrity_hash if last_entry else "0" * 64

        # Generar hash de integridad (Chained Hash)
        # Usamos el timestamp exacto que se guardará en la DB
        # Incluimos payload y headers en el hash para integridad total
        raw_data = f"{prev_hash}{threat_level}{attack_vector}{action_taken}{current_time.isoformat()}{json.dumps(payload_captured)}{json.dumps(headers_captured)}"
        integrity_hash = hashlib.sha256(raw_data.encode()).hexdigest()

        return cls.objects.create(
            timestamp=current_time, # Forzar el timestamp usado en el hash
            threat_level=threat_level,
            attack_vector=attack_vector,
            payload_captured=payload_captured,
            headers_captured=headers_captured,
            action_taken=action_taken,
            user=user,
            source_ip=source_ip,
            previous_hash=prev_hash,
            integrity_hash=integrity_hash
        )

    class Meta:
        verbose_name = "Forensic Security Log"
        verbose_name_plural = "Forensic Security Logs"
        ordering = ['-timestamp']

    def __str__(self):
        return f"[{self.threat_level}] {self.attack_vector} @ {self.timestamp}"


class PublicSystemAudit(models.Model):
    """
    Registro Público de Funciones y Auditorías Abiertas (Z-INSTITUTIONAL).
    Almacena resúmenes de actividad para transparencia ciudadana sin exponer datos sensibles.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    domain = models.CharField(max_length=50, help_text="Ej: Hacienda, Planeación, Salud")
    function_name = models.CharField(max_length=100, help_text="Nombre de la función pública asistida")
    impact_summary = models.TextField(help_text="Descripción del impacto social o administrativo")
    compliance_score = models.FloatField(default=1.0, help_text="Índice de cumplimiento normativo (0.0 a 1.0)")
    is_human_reviewed = models.BooleanField(default=False)

    # Referencia al log forense para auditores autorizados
    technical_trace_id = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Public System Audit Entry"
        verbose_name_plural = "Public System Audit"
        ordering = ['-timestamp']

    def __str__(self):
        return f"[{self.domain}] {self.function_name} - {self.timestamp.date()}"
