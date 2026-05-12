import logging

class RuntimeAnomalyDetector:
    def detect_latency_spike(self, component, latency):
        if latency > 1.0: # 1 second
             logging.warning(f"ANOMALY: {component} latency spike detected.")
             return True
        return False
