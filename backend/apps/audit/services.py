from .models import SystemAuditLog

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
