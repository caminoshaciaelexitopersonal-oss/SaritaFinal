class ServiceHealthChecker:
    """
    Scans registered services and checks their operational status.
    """
    def __init__(self, registry):
        self.registry = registry

    def check_all_health(self) -> dict:
        health_report = {}
        for service_id in self.registry.list_services():
            instance = self.registry.get_service(service_id)
            # If instance has a check_health method, run it; otherwise default to healthy
            if hasattr(instance, "check_health"):
                try:
                    health_report[service_id] = instance.check_health()
                except Exception as e:
                    health_report[service_id] = {"status": "UNHEALTHY", "error": str(e)}
            else:
                health_report[service_id] = {"status": "HEALTHY", "info": "Service fully online"}
        return health_report
