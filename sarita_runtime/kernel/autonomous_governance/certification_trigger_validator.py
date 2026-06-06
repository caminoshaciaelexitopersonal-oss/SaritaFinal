import time

class CertificationTriggerValidator:
    """
    Validates when a new certification should be requested.
    """
    def __init__(self, interval: int = 3600):
        self.interval = interval
        self.last_cert_time = 0

    def is_certification_required(self, state: dict):
        # 1. Time-based trigger
        if time.time() - self.last_cert_time > self.interval:
            return True

        # 2. Event-based trigger (e.g. key rotation, major drift)
        if state.get("critical_event"):
            return True

        return False
