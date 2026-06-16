class GlobalPrescriptiveGovernanceIndex:
    """
    Main engine for the Global Prescriptive Universality Index (GPUI).
    Scale: 0.0000 -> 1.0000
    """
    def __init__(self, calculator, ledger):
        self.calculator = calculator
        self.ledger = ledger

    def calculate_gpui(self, data):
        """
        Calculates GPUI using weighted sub-metrics.
        Weights: PR 25%, CC 20%, IE 20%, FS 20%, CA 15%.
        """
        metrics = self.calculator.calculate_metrics(data)

        gpui = (
            (metrics["predictive_reliability"] * 0.25) +
            (metrics["causal_confidence"] * 0.20) +
            (metrics["intervention_effectiveness"] * 0.20) +
            (metrics["future_stability"] * 0.20) +
            (metrics["civilizational_advantage"] * 0.15)
        )

        result = {
            "gpui_score": gpui,
            "metrics": metrics,
            "status": "CERTIFIED" if gpui >= 0.90 else "EXPERIMENTAL"
        }

        if self.ledger:
            self.ledger.record_gpui(result)

        return result
