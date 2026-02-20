import logging
import json
from django.utils import timezone

logger = logging.getLogger(__name__)

class EventBus:
    """
    Bus de eventos centralizado para la arquitectura event-driven.
    """
    _handlers = {}

    @classmethod
    def subscribe(cls, event_type, handler):
        if event_type not in cls._handlers:
            cls._handlers[event_type] = []
        cls._handlers[event_type].append(handler)

    @classmethod
    def publish(cls, event_type, payload, user=None):
        """
        Publica un evento y lo registra en el AuditEngine.
        """
        from apps.core_erp.audit_engine import AuditEngine

        logger.info(f"EVENT: {event_type} payload={payload}")

        # Auditoría obligatoria
        AuditEngine.log_event(
            event_type=event_type,
            payload=payload,
            user=user
        )

        # Ejecutar handlers (síncronos para esta fase)
        if event_type in cls._handlers:
            for handler in cls._handlers[event_type]:
                try:
                    handler(payload)
                except Exception as e:
                    logger.error(f"Error en handler para {event_type}: {e}")
