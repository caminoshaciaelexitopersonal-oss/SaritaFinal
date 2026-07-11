class ApiDiscovery:
    """
    Exposes and describes available system endpoints for secure, authenticated external systems.
    """
    def __init__(self, api_registry):
        self.registry = api_registry

    def discover_apis(self) -> dict:
        return {
            "api_version": "v1.32.0",
            "endpoints": {
                path: f"Sovereign API endpoint mapping to internal {res} service."
                for path, res in self.registry.routes.items()
            }
        }
