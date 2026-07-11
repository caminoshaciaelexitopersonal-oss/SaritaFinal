class ApiRegistry:
    """
    Maintains a registration index of official API paths and resource maps.
    """
    def __init__(self):
        self.routes = {}
        self._register_default_routes()

    def _register_default_routes(self):
        self.routes["/api/v1/health"] = "health"
        self.routes["/api/v1/state"] = "state"
        self.routes["/api/v1/events"] = "events"
        self.routes["/api/v1/optimize"] = "optimize"

    def register_route(self, path: str, resource: str):
        self.routes[path] = resource

    def exists(self, path: str) -> bool:
        return path in self.routes
