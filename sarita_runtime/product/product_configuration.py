class ProductConfiguration:
    """
    Manages runtime configuration settings, memory limits, and debug flags.
    """
    def __init__(self):
        self.settings = {
            "debug": False,
            "security_mode": "STRICT_IMMUNE",
            "max_memory_allocated_mb": 512,
            "persistence_enabled": True
        }

    def get(self, key: str, default=None):
        return self.settings.get(key, default)
