class PurposeRiskAnalyzer:
    """
    Analyzes risks to SARITA's sovereign purpose.
    """
    def analyze_risk(self, trajectory: dict):
        # Risk of drift, hijacking, or stagnation
        if not trajectory.get("is_converging"):
            return "HIGH", "Trajectory is diverging from target state."
        return "LOW", "Purpose alignment remains stable."
