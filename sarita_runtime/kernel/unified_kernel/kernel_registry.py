class KernelRegistry:
    """
    Registry indexing all active kernel-level components, namespaces, and APIs.
    """
    def __init__(self):
        self.components = {}

    def register_component(self, name: str, details: dict):
        self.components[name] = details

    def get_component(self, name: str) -> dict:
        return self.components.get(name, {})

    def list_components(self) -> list:
        return list(self.components.keys())
