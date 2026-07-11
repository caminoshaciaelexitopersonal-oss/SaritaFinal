from .event_catalog import EventCatalog
from .event_registry import EventRegistry
from .event_priority_manager import EventPriorityManager
from .event_subscriber_manager import EventSubscriberManager
from .event_router import EventRouter
from .event_stream import EventStream
from .event_history import EventHistory
from .event_dispatcher import EventDispatcher
from .event_replay_engine import EventReplayEngine

class UnifiedEventBus:
    """
    Unified Event Bus Facade for SARITA Phase 132.
    Acts as the sole communication medium across all cognitive components.
    """
    def __init__(self):
        self.catalog = EventCatalog()
        self.registry = EventRegistry()
        self.priority_mgr = EventPriorityManager()
        self.sub_mgr = EventSubscriberManager()
        self.router = EventRouter(self.sub_mgr)
        self.stream = EventStream()
        self.history = EventHistory()
        self.dispatcher = EventDispatcher(self.sub_mgr, self.router, self.history, self.stream)
        self.replay_engine = EventReplayEngine(self)

    def publish(self, event_type: str, data: dict, sender: str = "system") -> dict:
        """
        Publishes an event to the global stream and dispatches it to subscribers.
        """
        # Validate against registry
        if not self.registry.is_registered(event_type):
            self.registry.register_event(event_type)

        return self.dispatcher.dispatch(event_type, data, sender)

    def subscribe(self, event_pattern: str, handler):
        self.sub_mgr.subscribe(event_pattern, handler)

    def unsubscribe(self, event_pattern: str, handler):
        self.sub_mgr.unsubscribe(event_pattern, handler)

    def dispatch_locally(self, event):
        handlers = self.router.route_event(event)
        for h in handlers:
            try:
                h(event)
            except Exception:
                pass
