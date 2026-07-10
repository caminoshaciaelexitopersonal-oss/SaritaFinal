import time
from .api_registry import ApiRegistry
from .authentication_manager import AuthenticationManager
from .authorization_manager import AuthorizationManager
from .api_discovery import ApiDiscovery
from .api_health_monitor import ApiHealthMonitor
from .request_router import RequestRouter
from .service_dispatcher import ServiceDispatcher

class GlobalApiGateway:
    """
    Sovereign API Gateway (Phase 132).
    The single entrance boundary for all external and federated interface requests.
    Enforces Strict Cryptographic Tokens, Clearance Checks, and Service Dispatching.
    """
    def __init__(self):
        self.registry = ApiRegistry()
        self.auth = AuthenticationManager()
        self.acl = AuthorizationManager()
        self.discovery = ApiDiscovery(self.registry)
        self.health = ApiHealthMonitor()
        self.router = RequestRouter(self.registry, self.auth, self.acl)
        self.dispatcher = ServiceDispatcher()

    def process_external_call(self, path: str, headers: dict, action: str = "get_full_state", params: dict = None) -> dict:
        """
        Processes an incoming API request through authentication, authorization,
        routing, and service dispatching.
        """
        start_time = time.time()

        # 1. Route and Validate
        route_res = self.router.route_request(path, headers)
        if route_res["status"] != "ALLOWED":
            self.health.record_request(success=False, latency_ms=(time.time() - start_time) * 1000.0)
            return route_res

        # 2. Dispatch to internal back-end service
        dispatch_res = self.dispatcher.dispatch_to_service(
            resource=route_res["resource"],
            action=action,
            params=params
        )

        success = dispatch_res["status"] == "SUCCESS"
        self.health.record_request(success=success, latency_ms=(time.time() - start_time) * 1000.0)

        return dispatch_res
