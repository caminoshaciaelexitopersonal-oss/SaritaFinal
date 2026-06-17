class GlobalOptimalityEstimator:
    """Estimates the probability that the current best is the global optimum."""
    def estimate_global_optimality(self, arch, completeness):
        # Probability derived from coverage and fitness
        coverage = completeness.get("search_space_coverage", 0.0)
        return coverage * 0.98
