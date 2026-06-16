class PrescriptiveGovernanceCalculator:
    """
    Calculates sub-metrics for the Global Prescriptive Universality Index (GPUI).
    """
    def calculate_metrics(self, data):
        """
        Calculates reliability, confidence, effectiveness, stability, and advantage.
        """
        metrics = {
            "predictive_reliability": data.get("reliability", 0.95),
            "causal_confidence": data.get("causal_conf", 0.92),
            "intervention_effectiveness": data.get("effectiveness", 0.90),
            "future_stability": data.get("stability", 0.94),
            "civilizational_advantage": data.get("advantage", 0.88)
        }
        return metrics
