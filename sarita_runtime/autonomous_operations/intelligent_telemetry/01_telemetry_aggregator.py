import random

class TelemetryAggregator:
    def __init__(self):
        self.history = []

    def analyze_behavior(self, metric_stream):
        print("Performing AI-driven behavioral analysis on telemetry...")
        # Simulate anomaly correlation
        avg = sum(metric_stream) / len(metric_stream)
        anomalies = [x for x in metric_stream if x > avg * 1.5]

        if anomalies:
            return "ANOMALOUS_SPIKE_DETECTED"
        return "STABLE"

    def predict_pressure(self):
        # Linear regression mock for predictive pressure
        return random.uniform(0.1, 0.9)

if __name__ == "__main__":
    agg = TelemetryAggregator()
    stream = [10, 12, 11, 45, 10]
    print(f"Status: {agg.analyze_behavior(stream)}")
    print(f"Predicted Pressure: {agg.predict_pressure()}")
