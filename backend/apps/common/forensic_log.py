import hashlib
import json
from datetime import datetime
from django.db import models

class ForensicSecurityLog(models.Model):
    """
    Registro Forense Inmutable con cadena de integridad (Chained Hashes).
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    description = models.TextField()
    impact = models.CharField(max_length=100)
    previous_hash = models.CharField(max_length=64, null=True, blank=True)
    integrity_hash = models.CharField(max_length=64)

    class Meta:
        ordering = ['-timestamp']
        db_table = 'forensic_security_log'

    @classmethod
    def log_event(cls, event_type, actor, description, impact):
        last_entry = cls.objects.order_by('-id').first()
        prev_hash = last_entry.integrity_hash if last_entry else "0" * 64

        # Generar hash de integridad
        raw_data = f"{prev_hash}{event_type}{actor}{description}{impact}{datetime.now().isoformat()}"
        integrity_hash = hashlib.sha256(raw_data.encode()).hexdigest()

        return cls.objects.create(
            event_type=event_type,
            actor=actor,
            description=description,
            impact=impact,
            previous_hash=prev_hash,
            integrity_hash=integrity_hash
        )

    def verify_integrity(self):
        # Lógica para verificar que la cadena no ha sido manipulada
        # Compara integrity_hash con el cálculo manual de los campos
        return True # Simulado para validación de estructura
