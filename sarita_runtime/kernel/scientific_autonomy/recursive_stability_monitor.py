class RecursiveStabilityMonitor:
    def monitor_stability(self, history):
        # Monitors if recursive audits are converging or oscillating
        if len(history) < 2:
            return 1.0
        deltas = [abs(history[i] - history[i-1]) for i in range(1, len(history))]
        avg_delta = sum(deltas) / len(deltas)
        return 1.0 / (1.0 + avg_delta)
