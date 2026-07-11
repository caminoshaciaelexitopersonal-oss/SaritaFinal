class ComparisonFramework:
    """
    Formally compares current live results against standard baseline reference configurations under identical experimental protocols.
    """
    def __init__(self, baseline_repo):
        self.baseline_repo = baseline_repo

    def compare(self, current_runs: dict) -> dict:
        results = {}
        for key, val in current_runs.items():
            baseline_val = self.baseline_repo.get_reference_value(key)
            if baseline_val is not None:
                results[key] = {
                    "current": val,
                    "baseline": baseline_val,
                    "absolute_diff": round(val - baseline_val, 4),
                    "relative_improvement": round((val - baseline_val) / baseline_val, 4) if baseline_val > 0 else 0.0
                }
        return results
