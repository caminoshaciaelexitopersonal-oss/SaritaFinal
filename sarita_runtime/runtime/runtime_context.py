import time

class RuntimeContext:
    """
    State context block representing current global system runtime properties.
    """
    def __init__(self):
        self.context_id = "CTX-MASTER-001"
        self.start_time = time.time()
        self.attributes = {
            "mode": "SOVEREIGN_PRODUCTION",
            "log_level": "INFO",
            "max_memory_allocated": 256.0
        }

    def update_attribute(self, key: str, val):
        self.attributes[key] = val
