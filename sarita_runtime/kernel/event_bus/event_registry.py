from .event_catalog import EventCatalog

class EventRegistry:
    """
    Registry for event metadata definitions and validation rules.
    """
    def __init__(self):
        self.registered_events = {}
        self._register_defaults()

    def _register_defaults(self):
        for name in dir(EventCatalog):
            if not name.startswith("__") and isinstance(getattr(EventCatalog, name), str):
                self.register_event(getattr(EventCatalog, name))

    def register_event(self, event_type: str, metadata: dict = None):
        self.registered_events[event_type] = metadata or {"validated": True}

    def is_registered(self, event_type: str) -> bool:
        return event_type in self.registered_events
