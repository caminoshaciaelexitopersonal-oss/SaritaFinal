from sarita_runtime.kernel.unified_kernel.service_locator import ServiceLocator

class ServiceDispatcher:
    """
    Dispatches routed gateway calls to actual registered back-end kernel services.
    """
    def __init__(self):
        pass

    def dispatch_to_service(self, resource: str, action: str, params: dict = None) -> dict:
        """
        Locates the target service and dispatches the action with parameters.
        """
        # Resolve service identifier based on resource
        service_id = f"service.{resource}"
        instance = ServiceLocator.locate(service_id)

        if not instance:
            # We also try exact matching or direct fallback to state manager/event bus
            if resource == "state":
                instance = ServiceLocator.locate("service.state_manager")
            elif resource == "events":
                instance = ServiceLocator.locate("service.event_bus")

        if not instance:
            return {"status": "SERVICE_UNAVAILABLE", "error": f"Backend service {service_id} not located."}

        # Dispatch action based on type
        if hasattr(instance, action):
            try:
                method = getattr(instance, action)
                res = method(**(params or {}))
                return {"status": "SUCCESS", "data": res}
            except Exception as e:
                return {"status": "ERROR", "error": str(e)}
        else:
            # Default fallback data if specific action method doesn't exist
            if hasattr(instance, "get_full_state"):
                return {"status": "SUCCESS", "data": instance.get_full_state()}
            return {"status": "BAD_REQUEST", "error": f"Service does not expose action: {action}"}
