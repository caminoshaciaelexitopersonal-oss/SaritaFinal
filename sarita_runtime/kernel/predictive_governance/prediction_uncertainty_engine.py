class PredictionUncertaintyEngine:
    """
    Engine for quantifying and managing predictive uncertainty.
    """
    def __init__(self, epistemic_analyzer, aleatory_analyzer, interval_calc, ledger):
        self.epistemic_analyzer = epistemic_analyzer
        self.aleatory_analyzer = aleatory_analyzer
        self.interval_calc = interval_calc
        self.ledger = ledger

    def quantify_uncertainty(self, prediction, multiversal_data):
        """
        Calculates total predictive uncertainty and confidence intervals.
        """
        epistemic = self.epistemic_analyzer.analyze(None, multiversal_data)
        aleatory = self.aleatory_analyzer.analyze(0.1) # Sample variance

        total_uncertainty = (epistemic + aleatory) / 2.0

        intervals = {
            "95%": self.interval_calc.calculate_intervals(prediction, total_uncertainty, 0.95),
            "99%": self.interval_calc.calculate_intervals(prediction, total_uncertainty, 0.99),
            "99.9%": self.interval_calc.calculate_intervals(prediction, total_uncertainty, 0.999)
        }

        report = {
            "epistemic_uncertainty": epistemic,
            "aleatory_uncertainty": aleatory,
            "total_uncertainty": total_uncertainty,
            "intervals": intervals
        }

        if self.ledger:
            self.ledger.record_uncertainty_audit(report)

        return report
