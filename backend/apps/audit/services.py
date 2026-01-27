from typing import Optional, Dict, Any
from backend.models import AuditLog
from backend.api.models import CustomUser

def get_ip_from_request(request) -> Optional[str]:
    if not request:
        return None
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AuditLogger:
    @staticmethod
    def log(
        action: str,
        user: Optional[CustomUser] = None,
        request: Optional[Any] = None,
        details: Optional[Dict[str, Any]] = None
    ):
        log_username = "System"
        log_company = None
        if user:
            log_username = user.username
            if hasattr(user, 'perfil_prestador') and user.perfil_prestador:
                 log_company = user.perfil_prestador.company

        AuditLog.objects.create(
            user=user,
            username=log_username,
            company=log_company,
            action=action,
            ip_address=get_ip_from_request(request),
            details=details or {}
        )
