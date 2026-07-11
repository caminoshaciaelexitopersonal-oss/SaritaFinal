class ServiceRegistry:
    """
    Maintains a registration map of all active running services.
    """
    def __init__(self):
        self._services = {}

    def register(self, service_id: str, instance):
        self._services[service_id] = instance

    def unregister(self, service_id: str):
        if service_id in self._services:
            del self._services[service_id]

    def get_service(self, service_id: str):
        return self._services.get(service_id)

    def list_services(self) -> list:
        return list(self._services.keys())
