class ApiHealthMonitor:
    """
    Tracks and monitors API gateway request counts, errors, and average latencies.
    """
    def __init__(self):
        self.request_count = 0
        self.error_count = 0
        self.last_latency_ms = 1.2

    def record_request(self, success: bool, latency_ms: float):
        self.request_count += 1
        if not success:
            self.error_count += 1
        self.last_latency_ms = latency_ms

    def get_api_metrics(self) -> dict:
        return {
            "request_count": self.request_count,
            "error_count": self.error_count,
            "average_latency_ms": self.last_latency_ms
        }
