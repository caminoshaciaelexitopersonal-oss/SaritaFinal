import random

class HistoricalUnexpectedEventDetector:
    def __init__(self):
        self.anomalies = []

    def detect_unexpected(self, metrics, baseline):
        # Detect if metrics deviate significantly from baseline
        for key in metrics:
            if key in baseline:
                if abs(metrics[key] - baseline[key]) > 0.5:
                    anomaly = f"Sudden shift in {key}: {baseline[key]} -> {metrics[key]}"
                    self.anomalies.append(anomaly)
                    return anomaly

        # Random black swan events
        if random.random() < 0.05:
            anomaly = "Random Black Swan Event: Cognitive Convergence Spike"
            self.anomalies.append(anomaly)
            return anomaly

        return None
