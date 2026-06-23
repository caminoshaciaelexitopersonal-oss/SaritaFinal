class StagnationAnalyzer:
    def analyze_stagnation(self, performance_metrics):
        # Stagnation is detected when improvement rate drops below threshold
        improvement_rate = performance_metrics.get("improvement_delta", 1.0)
        return improvement_rate < 0.001
