import logging
from apps.core_erp.event_bus import EventBus
from .ledger_engine import LedgerEngine

logger = logging.getLogger(__name__)

class StandardAccountingHandlers:
    """
    Centralized event handlers for the LedgerEngine.
    Translates business events into Ledger impacts following Phase B flows.
    """

    @staticmethod
    def handle_business_event(event_type: str, payload: dict):
        """
        Generic handler that delegates to LedgerEngine.
        """
        logger.info(f"Accounting Handler: Processing {event_type}")
        try:
            LedgerEngine.post_event(event_type, payload)
        except Exception as e:
            logger.error(f"Failed to process accounting for {event_type}: {e}")
            # In a production system, we would move this to a Dead Letter Queue

    @staticmethod
    def register_all():
        """
        Registers all standard financial handlers in the EventBus.
        """
        standard_events = [
            'RESERVATION_CONFIRMED',
            'ReservationConfirmed',
            'PaymentReceived',
            'ProviderPaid',
            'SALE',
            'LIQUIDATION'
        ]

        for event in standard_events:
            EventBus.subscribe(event, lambda p, et=event: StandardAccountingHandlers.handle_business_event(et, p))

        logger.info("Standard Accounting Handlers registered.")
