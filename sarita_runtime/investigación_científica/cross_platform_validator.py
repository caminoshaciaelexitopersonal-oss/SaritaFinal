class CrossPlatformValidator:
    """
    Validates experimental consistency across multiple logical architectures, operating systems, and platforms.
    """
    def __init__(self):
        pass

    def validate_across_platforms(self, run_results_per_platform: dict) -> dict:
        if not run_results_per_platform:
            return {"consistent": True, "max_delta": 0.0}

        means = {}
        for platform, data in run_results_per_platform.items():
            if data:
                means[platform] = sum(data) / len(data)

        if len(means) < 2:
            return {"consistent": True, "max_delta": 0.0}

        val_list = list(means.values())
        max_delta = max(val_list) - min(val_list)
        consistent = max_delta < 0.02

        return {
            "platform_means": {k: round(v, 4) for k, v in means.items()},
            "max_delta": round(max_delta, 4),
            "consistent": consistent
        }
