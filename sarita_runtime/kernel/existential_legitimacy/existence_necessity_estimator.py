class ExistenceNecessityEstimator:
    """
    Estimates the necessity of SARITA's existence.
    """
    def estimate_necessity(self, absence_impact: float, replacement_feasibility: bool):
        if not replacement_feasibility:
            return absence_impact * 2.0 # Necessity doubled if no replacement exists
        return absence_impact
