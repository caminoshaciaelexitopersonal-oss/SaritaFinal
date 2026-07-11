class IndependentReproduction:
    """
    Coordinates and validates the autonomous replication of studies conducted on external/decoupled hosts.
    """
    def __init__(self):
        pass

    def verify_reproduction(self, original_metrics: dict, replicated_metrics: dict) -> dict:
        divergences = {}
        for key, original_val in original_metrics.items():
            replicated_val = replicated_metrics.get(key)
            if replicated_val is None:
                divergences[key] = "MISSING_IN_REPLICATION"
            else:
                diff = abs(original_val - replicated_val)
                divergences[key] = {
                    "original": original_val,
                    "replicated": replicated_val,
                    "difference": round(diff, 4),
                    "reproduced": diff < 0.05
                }

        success = all(isinstance(v, dict) and v["reproduced"] for v in divergences.values())

        return {
            "reproduction_verified": success,
            "metric_divergences": divergences
        }
