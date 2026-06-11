class ForecastHorizonValidator:
    """
    Main engine for auditing and certifying predictive horizons.
    """
    def __init__(self, reliability_engine, distance_calc, limit_detector, ledger):
        self.reliability_engine = reliability_engine
        self.distance_calc = distance_calc
        self.limit_detector = limit_detector
        self.ledger = ledger

    def validate_horizon(self, model_id, target_horizon):
        """
        Determines and certifies the maximum reliable horizon.
        """
        reliability = self.reliability_engine.evaluate_reliability(target_horizon)
        limit = self.limit_detector.detect_limit(None)

        is_reliable = reliability >= 0.95 and target_horizon <= limit

        audit = {
            "target_horizon": target_horizon,
            "max_reliable_horizon": limit,
            "reliability_score": reliability,
            "status": "CERTIFIED" if is_reliable else "SPECULATIVE"
        }

        if self.ledger:
            self.ledger.record_horizon_audit(audit)

        return audit
