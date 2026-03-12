from .models import SystemAuditLog

class AuditLogger:
    @staticmethod
    def log_action(user, action, details, ip_address=None):
        """
        Mock compatibility with DocumentCoordinatorService expectations.
        """
        return SystemAuditLog.objects.create(
            user=user,
            action=action,
            entity="AuditLog",
            entity_id="0",
            ip_address=ip_address or "0.0.0.0",
            new_values=details
        )

class AuditService:
    @staticmethod
    def log(user, action, entity, entity_id, ip_address, old=None, new=None):
        return SystemAuditLog.objects.create(
            user=user,
            action=action,
            entity=entity,
            entity_id=str(entity_id),
            ip_address=ip_address,
            old_values=old,
            new_values=new
        )
