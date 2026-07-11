from .runtime_recovery_engine import RuntimeRecoveryEngine

class RuntimeSupervisor:
    """
    Supervises the health state of all registered services and triggers recovery when appropriate.
    """
    def __init__(self, master):
        self.master = master
        self.recovery_engine = RuntimeRecoveryEngine(self)

    def verify_service_health(self) -> dict:
        """
        Scans all services and runs recovery on unhealthy ones.
        """
        report = self.master.kernel.service_health.check_all_health()
        for svc_id, status_data in report.items():
            if status_data.get("status") == "UNHEALTHY":
                self.recovery_engine.attempt_recovery(svc_id)
        return report
