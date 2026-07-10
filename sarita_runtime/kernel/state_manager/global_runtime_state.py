import time

class GlobalRuntimeState:
    """
    Manages physical master process status, threads, sessions, and memory allocations.
    """
    def __init__(self):
        self.status = "OFFLINE"
        self.uptime_start = 0.0
        self.session_count = 0
        self.cpu_usage_pct = 5.0
        self.memory_allocated_mb = 120.0

    def set_status(self, new_status: str):
        self.status = new_status
        if new_status == "ONLINE" and self.uptime_start == 0.0:
            self.uptime_start = time.time()
        elif new_status == "OFFLINE":
            self.uptime_start = 0.0

    def to_dict(self) -> dict:
        uptime = round(time.time() - self.uptime_start, 2) if self.uptime_start > 0.0 else 0.0
        return {
            "status": self.status,
            "uptime_sec": uptime,
            "session_count": self.session_count,
            "cpu_usage_pct": self.cpu_usage_pct,
            "memory_allocated_mb": self.memory_allocated_mb
        }
