import hashlib
import json
import logging
from django.utils import timezone
from apps.admin_plataforma.models import GovernanceAuditLog

logger = logging.getLogger(__name__)

class AuditEngine:
    """
    Motor de Auditoría Centralizado (Core ERP).
    Asegura la inmutabilidad de los registros mediante hash chaining.
    """

    @staticmethod
    def log_event(event_type, payload, user=None):
        """
        Registra un evento con integridad garantizada.
        """
        try:
            # Obtener el último log para encadenar
            last_log = GovernanceAuditLog.objects.order_by('-timestamp').first()
            previous_hash = last_log.integrity_hash if last_log else "GENESIS_COMMERCIAL_ENGINE"

            # Crear entrada
            log_entry = GovernanceAuditLog(
                usuario=user,
                intencion=event_type,
                parametros=payload,
                resultado={"status": "AUDITED"},
                timestamp=timezone.now()
            )

            # Calcular Hash SHA-256 (RC-S Hardening)
            payload_str = json.dumps(payload, sort_keys=True)
            raw_data = f"{event_type}{payload_str}{log_entry.timestamp}{previous_hash}"
            log_entry.integrity_hash = hashlib.sha256(raw_data.encode()).hexdigest()
            log_entry.previous_hash = previous_hash

            log_entry.save()
            logger.info(f"AUDIT: {event_type} - Hash: {log_entry.integrity_hash[:8]}")
            return log_entry
        except Exception as e:
            logger.error(f"Fallo crítico en AuditEngine: {e}")
            return None
