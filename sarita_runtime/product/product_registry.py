class ProductRegistry:
    """
    Catalog registry indexing all operational subsystems, engines, and gateways.
    """
    def __init__(self):
        self.registrations = {}

    def register_subsystem(self, key: str, details: dict):
        self.registrations[key] = details

    def get_subsystem(self, key: str) -> dict:
        return self.registrations.get(key, {})

    def list_subsystems(self) -> list:
        return list(self.registrations.keys())
