import random

class HealthMatrix:
    def __init__(self):
        self.domains = ["FINANCE", "AI", "ORCHESTRATION", "GOVERNANCE"]

    def evaluate_ecosystem(self):
        health_report = {}
        for domain in self.domains:
            score = random.uniform(0.7, 1.0) # Simulate health score
            health_report[domain] = {
                "status": "HEALTHY" if score > 0.8 else "DEGRADED",
                "score": round(score, 2)
            }
        return health_report

class PressureDetector:
    def detect_saturation(self, metrics):
        # Checks for event lag or high CPU
        if metrics.get('kafka_lag', 0) > 1000:
            return "CRITICAL_LAG_DETECTED"
        return "STABLE"

if __name__ == "__main__":
    hm = HealthMatrix()
    pd = PressureDetector()
    report = hm.evaluate_ecosystem()
    print(f"Global Health Report: {report}")
    print(f"Pressure Check: {pd.detect_saturation({'kafka_lag': 500})}")
