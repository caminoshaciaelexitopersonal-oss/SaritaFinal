import hashlib
import json
import logging
from django.utils import timezone

logger = logging.getLogger(__name__)

class AuditEngine:
    """
    Motor de auditoría sistémica del Core ERP.
    Garantiza trazabilidad de cambios financieros.
    """

    @staticmethod
    def generate_integrity_hash(data_dict, previous_hash):
        """
        Genera un hash SHA-256 encadenado para garantizar inmutabilidad.
        """
        payload = {
            "data": data_dict,
            "previous_hash": previous_hash,
            "system_timestamp": timezone.now().isoformat()
        }
        encoded_data = json.dumps(payload, sort_keys=True).encode()
        return hashlib.sha256(encoded_data).hexdigest()

    @staticmethod
    def audit_transaction(user, action, model_name, object_id, changes):
        """
        Registra un evento de auditoría.
        """
        logger.info(f"AUDIT ERP: {user} realizó {action} en {model_name}/{object_id}. Cambios: {changes}")
        # En una implementación completa esto guardaría en un GovernanceAuditLog o similar
