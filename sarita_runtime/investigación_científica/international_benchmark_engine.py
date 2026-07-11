class InternationalBenchmarkEngine:
    """
    Compares SARITA indices to standard international/academic reference benchmark models.
    """
    def __init__(self, baseline_repo):
        self.baseline_repo = baseline_repo

    def evaluate_against_benchmarks(self, active_metrics: dict) -> dict:
        comparisons = {}
        for metric, val in active_metrics.items():
            ref = self.baseline_repo.get_reference_value(metric)
            if ref is not None:
                percent_gain = ((val - ref) / ref) * 100.0 if ref > 0 else 0.0
                comparisons[metric] = {
                    "active_value": val,
                    "reference_value": ref,
                    "gain_percent": round(percent_gain, 2),
                    "superior": val > ref
                }
        return comparisons
