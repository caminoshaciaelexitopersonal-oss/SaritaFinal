class ReproducibilityProtocol:
    """
    Enforces deterministic reproducibility schemas on runs and saves reproducibility scores.
    """
    def __init__(self):
        pass

    def calculate_reproducibility_score(self, run_a: dict, run_b: dict) -> dict:
        score = 1.0
        details = {}

        res_a = run_a.get("results", [])
        res_b = run_b.get("results", [])
        if len(res_a) != len(res_b):
            score -= 0.3
            details["length_mismatch"] = True
        else:
            diffs = []
            for i in range(len(res_a)):
                da = res_a[i].get("data")
                db = res_b[i].get("data")
                if isinstance(da, list) and isinstance(db, list):
                    for j in range(min(len(da), len(db))):
                        diffs.append(abs(da[j] - db[j]))
                elif isinstance(da, (int, float)) and isinstance(db, (int, float)):
                    diffs.append(abs(da - db))

            if diffs:
                avg_diff = sum(diffs) / len(diffs)
                score -= min(0.5, avg_diff * 0.5)
                details["average_value_difference"] = avg_diff

        env_a = run_a.get("environment_hash")
        env_b = run_b.get("environment_hash")
        if env_a != env_b:
            score -= 0.1
            details["environment_mismatch"] = True

        score = max(0.0, min(1.0, score))
        return {
            "reproducibility_score": round(score, 4),
            "status": "FULLY_REPRODUCIBLE" if score > 0.95 else "PARTIALLY_REPRODUCIBLE",
            "comparison_details": details
        }
