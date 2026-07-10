import time
import uuid

class EventDispatcher:
    """
    Orchestrates the synchronous and asynchronous dispatching of events.
    """
    def __init__(self, subscriber_mgr, router, history, stream):
        self.sub_mgr = subscriber_mgr
        self.router = router
        self.history = history
        self.stream = stream

    def dispatch(self, event_type: str, data: dict, sender: str = "system") -> dict:
        """
        Synthesizes an event payload, dispatches it to routed handlers,
        and records it in the history registry.
        """
        event = {
            "event_id": f"EVT-{uuid.uuid4().hex[:8].upper()}",
            "type": event_type,
            "sender": sender,
            "timestamp": time.time(),
            "data": data
        }

        # Route event to handlers
        handlers = self.router.route_event(event)
        execution_results = []

        for handler in handlers:
            try:
                res = handler(event)
                execution_results.append({"handler": str(handler), "status": "SUCCESS", "res": res})
            except Exception as e:
                execution_results.append({"handler": str(handler), "status": "ERROR", "error": str(e)})

        # Log to stream and history
        self.stream.append(event)
        self.history.record_event(event)

        return {
            "event": event,
            "handlers_called": len(handlers),
            "results": execution_results
        }
