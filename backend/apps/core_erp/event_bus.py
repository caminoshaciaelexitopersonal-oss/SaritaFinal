import logging

logger = logging.getLogger(__name__)

class EventBus:
    """
    Bus de Eventos Central del Core ERP.
    Implementa el patrón Pub/Sub para desacoplar los módulos del sistema.
    Garantiza que la lógica de negocio no dependa de importaciones directas circulares.
    """

    # Tipos de Eventos Estándar
    INVOICE_CREATED = 'INVOICE_CREATED'
    PAYMENT_RECEIVED = 'PAYMENT_RECEIVED'
    JOURNAL_POSTED = 'JOURNAL_POSTED'
    SUBSCRIPTION_ACTIVATED = 'SUBSCRIPTION_ACTIVATED'
    SUBSCRIPTION_CANCELLED = 'SUBSCRIPTION_CANCELLED'
    PLAN_UPGRADED = 'PLAN_UPGRADED'
    PLAN_DOWNGRADED = 'PLAN_DOWNGRADED'
    USAGE_RECORDED = 'USAGE_RECORDED'
    PERIOD_CLOSED = 'PERIOD_CLOSED'
    CHURN_RISK_ALERT = 'CHURN_RISK_ALERT'

    _subscribers = {}

    @classmethod
    def subscribe(cls, event_type, callback):
        """
        Registra un suscriptor para un tipo de evento específico.
        """
        if event_type not in cls._subscribers:
            cls._subscribers[event_type] = []
        cls._subscribers[event_type].append(callback)
        logger.info(f"Suscriptor registrado para el evento: {event_type}")

    @classmethod
    def emit(cls, event_type, payload):
        """
        Dispara un evento y notifica a todos sus suscriptores.
        Incluye auditoría automática y propagación de correlation_id.
        """
        from .observability.middleware import get_correlation_id
        from .models import EventAuditLog
        import uuid

        correlation_id = get_correlation_id()
        tenant_id = payload.get('tenant_id')

        logger.info(f"Emitiendo evento ERP: {event_type} (CID: {correlation_id})")

        # 1. Crear Registro de Auditoría (Fase 5.3)
        audit_entry = EventAuditLog.objects.create(
            event_type=event_type,
            correlation_id=correlation_id,
            tenant_id=tenant_id,
            payload=payload,
            status='EMITTED'
        )

        subscribers = cls._subscribers.get(event_type, [])
        success_count = 0

        for callback in subscribers:
            try:
                # Inyectar correlation_id si es necesario (propagación)
                payload['_correlation_id'] = correlation_id
                callback(payload)
                success_count += 1
            except Exception as e:
                logger.error(f"Error procesando suscriptor de {event_type}: {str(e)}")
                audit_entry.status = 'PARTIAL_FAILURE'
                audit_entry.error_details = (audit_entry.error_details or "") + f"\nCallback error: {str(e)}"

        if success_count == len(subscribers):
            audit_entry.status = 'PROCESSED'

        audit_entry.save()

    @classmethod
    def clear_subscribers(cls):
        """
        Limpia todos los suscriptores (útil para tests).
        """
        cls._subscribers = {}
# Architectural stabilization 2026
