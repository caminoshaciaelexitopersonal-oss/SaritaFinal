class EventRouter:
    """
    Routes events to specific subscribers and logs path traversal metadata.
    """
    def __init__(self, subscriber_manager):
        self.sub_mgr = subscriber_manager

    def route_event(self, event) -> list:
        """
        Determines target handler routes for a given event.
        """
        handlers = self.sub_mgr.get_handlers_for(event["type"])
        return handlers
