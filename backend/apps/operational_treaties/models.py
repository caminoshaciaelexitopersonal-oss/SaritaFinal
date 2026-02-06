from django.db import models
import uuid
import hashlib
import json
from django.utils import timezone

class OperationalTreaty(models.Model):
    """
    Tratados Operativos (Z-OPERATIONAL-TREATIES).
    Define los marcos técnicos y jurídicos de cooperación entre nodos.
    """
    class TreatyType(models.TextChoices):
        TIT = 'TIT', 'Tratado de Interoperabilidad Técnica'
        TNA = 'TNA', 'Tratado de Neutralidad Algorítmica'
        TNID = 'TNID', 'Tratado de No-Injerencia Digital'
        TSDS = 'TSDS', 'Tratado de Soberanía de Datos y Señales'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=TreatyType.choices)
    version = models.CharField(max_length=20, default='1.0')
    is_active = models.BooleanField(default=True)

    # Parámetros técnicos del tratado
    guardrails_config = models.JSONField(help_text="Configuración de límites algorítmicos para este tratado.")

    # Identificadores de los nodos participantes
    participating_nodes = models.JSONField(default=list, help_text="Lista de IDs de nodos soberanos firmantes.")

    signed_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_type_display()} v{self.version} ({self.name})"

class TreatyComplianceAudit(models.Model):
    """
    Auditoría de Cumplimiento de Tratados.
    Registra cada interacción y verifica que cumple con los guardrails del tratado.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    treaty = models.ForeignKey(OperationalTreaty, on_delete=models.CASCADE, related_name='audits')
    timestamp = models.DateTimeField(auto_now_add=True)

    actor_node_id = models.CharField(max_length=100)
    action_type = models.CharField(max_length=100, help_text="Ej: SIGNAL_EMISSION, MITIGATION_PROPOSAL")

    payload_summary = models.JSONField()
    is_compliant = models.BooleanField(default=True)
    violation_details = models.TextField(null=True, blank=True)

    # Hash de integridad encadenado (RC-S Hardening)
    previous_hash = models.CharField(max_length=64, null=True, blank=True)
    integrity_hash = models.CharField(max_length=64, null=True, blank=True)

    def generate_hash(self, prev_hash):
        data = f"{prev_hash}{self.treaty.id}{self.timestamp.isoformat()}{json.dumps(self.payload_summary)}{self.is_compliant}"
        return hashlib.sha256(data.encode()).hexdigest()

    class Meta:
        ordering = ['-timestamp']

class SovereignKillSwitch(models.Model):
    """
    Kill-Switch Soberano para Tratados.
    Permite la desconexión inmediata de interoperabilidad.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    treaty = models.OneToOneField(OperationalTreaty, on_delete=models.CASCADE, related_name='kill_switch')
    is_triggered = models.BooleanField(default=False)

    triggered_at = models.DateTimeField(null=True, blank=True)
    triggered_by = models.ForeignKey('api.CustomUser', on_delete=models.SET_NULL, null=True)
    reason = models.TextField()

    # Nivel de bloqueo
    # 1: Informativo (Alertas activas)
    # 2: Operativo (Suspende misiones compartidas)
    # 3: Total (Cierre de Diplomatic Gateway para este tratado)
    block_level = models.IntegerField(default=3)

    def trigger(self, user, reason):
        self.is_triggered = True
        self.triggered_at = timezone.now()
        self.triggered_by = user
        self.reason = reason
        self.save()

        # Desactivar el tratado
        self.treaty.is_active = False
        self.treaty.save()

    def __str__(self):
        return f"Kill-Switch: {self.treaty.name} (Active: {not self.is_triggered})"
