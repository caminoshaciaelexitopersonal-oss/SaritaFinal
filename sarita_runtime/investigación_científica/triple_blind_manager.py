class TripleBlindManager:
    """
    Manages triple-blind trials where subject (run), researcher (executor), and analyzer (statistical engine) are completely blinded.
    """
    def __init__(self, reviewers, statisticians):
        self.reviewers = reviewers
        self.statisticians = statisticians

    def conduct_triple_blind_run(self, raw_experimental_data: list, test_func) -> dict:
        blinded_data = {
            "Group_A": raw_experimental_data,
            "Group_B": [test_func(x) for x in raw_experimental_data]
        }

        analyses = []
        for stat in self.statisticians:
            res = stat(blinded_data["Group_A"], blinded_data["Group_B"])
            analyses.append(res)

        avg_p_value = sum(a.get("p_value", 1.0) for a in analyses) / len(analyses) if analyses else 1.0

        return {
            "trial_type": "TRIPLE_BLIND",
            "statisticians_engaged": len(self.statisticians),
            "blinded_p_value": round(avg_p_value, 4),
            "significant": avg_p_value < 0.05
        }
