class RequestRouter:
    """
    Resolves request paths to active endpoints and applies authentication/authorization checks.
    """
    def __init__(self, api_registry, auth_manager, acl_manager):
        self.registry = api_registry
        self.auth = auth_manager
        self.acl = acl_manager

    def route_request(self, path: str, headers: dict) -> dict:
        """
        Processes path routing, authentication, and authorization clearance.
        """
        if not self.registry.exists(path):
            return {"status": "NOT_FOUND", "code": 404, "error": f"Path '{path}' not registered."}

        # 1. Authenticate
        if not self.auth.authenticate_request(headers):
            return {"status": "UNAUTHORIZED", "code": 401, "error": "Invalid or missing Bearer token."}

        # 2. Authorize
        clearance = headers.get("X-Clearance", "STANDARD")
        if not self.acl.authorize_action(path, clearance):
            return {"status": "FORBIDDEN", "code": 403, "error": "Insufficient sovereign clearance level."}

        # Successful routing
        return {
            "status": "ALLOWED",
            "code": 200,
            "resource": self.registry.routes[path]
        }
