class ConfidenceDecayEngine:
    """
    Engine for measuring and modeling the temporal degradation of predictions.
    """
    def __init__(self, tracker, monitor, half_life_calc, ledger):
        self.tracker = tracker
        self.monitor = monitor
        self.half_life_calc = half_life_calc
        self.ledger = ledger

    def measure_decay(self, forecast_id):
        """
        Generates the Confidence Decay Curve.
        """
        accuracy_map = self.tracker.track_accuracy(forecast_id)
        stability = self.monitor.monitor_stability(None)
        half_life = self.half_life_calc.calculate_half_life(accuracy_map)

        report = {
            "decay_curve": accuracy_map,
            "forecast_stability": stability,
            "accuracy_half_life": half_life
        }

        if self.ledger:
            self.ledger.record_temporal_decay(report)

        return report
