class FrontierValueEstimator:
    def estimate_value(self, frontier):
        # Estimates the potential value of a new frontier expansion
        complexity = frontier.get("complexity", 1.0)
        uniqueness = frontier.get("uniqueness", 1.0)
        return complexity * uniqueness
