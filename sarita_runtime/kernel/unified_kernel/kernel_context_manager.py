class KernelContextManager:
    """
    Manages active operational contexts, scopes, and isolation boundaries.
    """
    def __init__(self):
        self.active_context = {
            "scope": "SOVEREIGN_SYSTEM",
            "clearance": "MAXIMUM",
            "active_epoch": 1
        }

    def set_context(self, scope: str, clearance: str):
        self.active_context["scope"] = scope
        self.active_context["clearance"] = clearance

    def get_context(self) -> dict:
        return self.active_context
