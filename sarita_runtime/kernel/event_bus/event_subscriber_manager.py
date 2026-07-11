import collections

class EventSubscriberManager:
    """
    Manages subscriber handlers for the Unified Event Bus.
    Supports wildcard event matching.
    """
    def __init__(self):
        self.subscribers = collections.defaultdict(list)

    def subscribe(self, event_pattern: str, handler):
        """
        Subscribes a callback to an event pattern.
        """
        if handler not in self.subscribers[event_pattern]:
            self.subscribers[event_pattern].append(handler)

    def unsubscribe(self, event_pattern: str, handler):
        if handler in self.subscribers[event_pattern]:
            self.subscribers[event_pattern].remove(handler)

    def get_handlers_for(self, event_type: str) -> list:
        """
        Matches exact topics or wildcard structures (e.g. state.*).
        """
        matched = []
        for pattern, handlers in self.subscribers.items():
            if pattern == "*" or pattern == event_type:
                matched.extend(handlers)
            elif pattern.endswith(".*") and event_type.startswith(pattern[:-2]):
                matched.extend(handlers)
        return list(set(matched))
