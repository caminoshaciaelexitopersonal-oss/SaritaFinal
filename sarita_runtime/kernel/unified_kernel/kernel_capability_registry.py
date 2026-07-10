class KernelCapabilityRegistry:
    """
    Registry for operational capabilities, modules, and engine feature maps.
    """
    def __init__(self):
        self.capabilities = {}

    def register_capability(self, name: str, version: str, active: bool = True):
        self.capabilities[name] = {
            "version": version,
            "active": active
        }

    def is_active(self, name: str) -> bool:
        cap = self.capabilities.get(name)
        return cap["active"] if cap else False
