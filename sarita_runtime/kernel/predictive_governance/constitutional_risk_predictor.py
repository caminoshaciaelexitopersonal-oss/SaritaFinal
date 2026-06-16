import math

class ConstitutionalRiskPredictor:
    """
    Predicts institutional risks and degradation within a constitution.
    """
    def predict_risk(self, current_state):
        """
        Analyzes current state to predict future risk levels using exponential decay modeling.
        """
        legitimacy = current_state.get("legitimacy", 1.0)
        adaptation = current_state.get("adaptation", 1.0)

        # Risk increases exponentially as legitimacy or adaptation falls
        risk_score = 1.0 - (legitimacy * adaptation)

        if risk_score > 0.8:
            return "EXISTENTIAL"
        elif risk_score > 0.6:
            return "CRITICAL"
        elif risk_score > 0.4:
            return "HIGH"
        elif risk_score > 0.2:
            return "MODERATE"
        return "LOW"
