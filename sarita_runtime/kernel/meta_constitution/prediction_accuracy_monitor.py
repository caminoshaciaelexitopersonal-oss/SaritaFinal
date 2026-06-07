class PredictionAccuracyMonitor:
    """
    Compares predicted outcomes vs actual outcomes to calculate accuracy.
    """
    def __init__(self):
        self.history = []

    def monitor_accuracy(self, prediction: dict, actual_outcome: dict):
        predicted_stability = prediction.get("predicted_stability")
        actual_stability = actual_outcome.get("actual_stability")

        delta = abs(predicted_stability - actual_stability)
        accuracy = max(0, 1.0 - delta)

        entry = {
            "entity_id": prediction.get("amendment_id"),
            "predicted": predicted_stability,
            "actual": actual_stability,
            "delta": delta,
            "accuracy": accuracy
        }
        self.history.append(entry)
        return entry

    def get_average_accuracy(self):
        if not self.history:
            return 1.0
        return sum(h["accuracy"] for h in self.history) / len(self.history)
