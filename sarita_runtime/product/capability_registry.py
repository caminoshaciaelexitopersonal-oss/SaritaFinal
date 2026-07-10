class ProductCapabilityRegistry:
    """
    Registry for product-level capabilities, mapping physical phases to active features.
    """
    def __init__(self):
        self.capabilities = {}

    def register(self, key: str, value: dict):
        self.capabilities[key] = value

    def is_active(self, key: str) -> bool:
        cap = self.capabilities.get(key)
        return cap.get("active", False) if cap else False
