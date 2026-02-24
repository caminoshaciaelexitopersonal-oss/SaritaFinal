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
        """
        logger.info(f"Emitiendo evento ERP: {event_type}")
        subscribers = cls._subscribers.get(event_type, [])

        for callback in subscribers:
            try:
                callback(payload)
            except Exception as e:
                logger.error(f"Error procesando suscriptor de {event_type}: {str(e)}")

    @classmethod
    def clear_subscribers(cls):
        """
        Limpia todos los suscriptores (útil para tests).
        """
        cls._subscribers = {}
# Architectural stabilization 2026
