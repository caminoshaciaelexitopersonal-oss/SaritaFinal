class UnknownUnknownsEstimator:
    """Estimates the impact of unexplored design spaces on global optimality."""
    def estimate_unknown_unknowns(self, completeness_res):
        # Inverse relationship with coverage
        factor = 1.0 - completeness_res.get("search_space_coverage", 0.0)
        return {"factor": factor, "risk_multiplier": 1.0 + factor}
