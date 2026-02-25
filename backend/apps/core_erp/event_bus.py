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
    _async_events = [
        'INVOICE_CREATED', 'SUBSCRIPTION_ACTIVATED', 'SUBSCRIPTION_CANCELLED',
        'PLAN_UPGRADED', 'PLAN_DOWNGRADED', 'USAGE_RECORDED', 'CHURN_RISK_ALERT'
    ]

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
        Implementa separación síncrono/asíncrono y reintentos (Fase 6.2).
        """
        from .observability.middleware import get_correlation_id
        from .models import EventAuditLog
        import time

        correlation_id = get_correlation_id()
        tenant_id = payload.get('tenant_id')

        logger.info(f"Emitiendo evento ERP: {event_type} (CID: {correlation_id})")

        # 1. Auditoría Inmediata
        audit_entry = EventAuditLog.objects.create(
            event_type=event_type,
            correlation_id=correlation_id,
            tenant_id=tenant_id,
            payload=payload,
            status='EMITTED'
        )

        subscribers = cls._subscribers.get(event_type, [])

        # 2. Ejecución (Síncrona vs Asíncrona)
        if event_type in cls._async_events:
            # En una implementación real, aquí se encolaría en Celery/Redis
            # Para este ERP, simulamos el disparo asíncrono
            logger.info(f"Evento {event_type} marcado como ASÍNCRONO.")
            cls._dispatch_async(event_type, payload, subscribers, audit_entry)
        else:
            # Ejecución Síncrona con Reintentos (Smart Retry)
            cls._dispatch_sync_with_retry(event_type, payload, subscribers, audit_entry)

    @classmethod
    def _dispatch_sync_with_retry(cls, event_type, payload, subscribers, audit_entry):
        """
        Ejecuta suscriptores de forma síncrona con backoff exponencial.
        """
        success_count = 0
        max_retries = 3

        for callback in subscribers:
            attempt = 0
            while attempt < max_retries:
                try:
                    payload['_correlation_id'] = audit_entry.correlation_id
                    callback(payload)
                    success_count += 1
                    break
                except Exception as e:
                    attempt += 1
                    wait_time = 2 ** attempt
                    logger.error(f"Error en {event_type} (intento {attempt}): {str(e)}. Reintentando en {wait_time}s...")
                    time.sleep(wait_time)
                    if attempt == max_retries:
                        audit_entry.status = 'PARTIAL_FAILURE'
                        audit_entry.error_details = (audit_entry.error_details or "") + f"\nCallback failed after {max_retries} retries: {str(e)}"

        if success_count == len(subscribers):
            audit_entry.status = 'PROCESSED'
        audit_entry.save()

    @classmethod
    def _dispatch_async(cls, event_type, payload, subscribers, audit_entry):
        """
        Punto de integración para colas persistentes (Fase 6.2.2).
        """
        # Placeholder para Celery: task_dispatch_event.delay(event_type, payload)
        # Por ahora ejecutamos síncronamente pero marcamos el estado.
        for callback in subscribers:
            try:
                callback(payload)
            except Exception as e:
                logger.error(f"Async simulation failed for {event_type}: {e}")

        audit_entry.status = 'QUEUED_COMPLETED'
        audit_entry.save()

    @classmethod
    def clear_subscribers(cls):
        """
        Limpia todos los suscriptores (útil para tests).
        """
        cls._subscribers = {}
# Architectural stabilization 2026
