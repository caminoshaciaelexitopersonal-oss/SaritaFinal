class ConstitutionalPredictionEngine:
    """
    Main engine for universal constitutional prediction.
    """
    def __init__(self, future_gen, risk_pred, stability_forecaster, ledger):
        self.future_gen = future_gen
        self.risk_pred = risk_pred
        self.stability_forecaster = stability_forecaster
        self.ledger = ledger

    def predict_evolution(self, current_state, trajectory_data):
        """
        Predicts constitutional evolution and detects optimal reforms.
        """
        futures = self.future_gen.generate_futures(current_state, trajectory_data)
        risk = self.risk_pred.predict_risk(current_state)
        # Use trajectory data as pressures
        stability = self.stability_forecaster.forecast_stability(current_state, trajectory_data)

        prediction = {
            "futures": futures,
            "risk_level": risk,
            "stability_score": stability,
            "optimal_reforms": self._identify_optimal_reforms(current_state, futures)
        }

        if self.ledger:
            self.ledger.record_prediction("CONSTITUTIONAL", prediction)

        return prediction

    def _identify_optimal_reforms(self, state, futures):
        """
        Detects reforms that maximize stability in future horizons.
        """
        optimal = []
        if state.get("legitimacy", 1.0) < 0.8:
            optimal.append("REFORM-LEGITIMACY-STRENGTHENING")
        if state.get("adaptation", 1.0) < 0.8:
            optimal.append("REFORM-ADAPTIVE-AUTHORITY-SHIFT")

        if not optimal:
            optimal.append("REFORM-MAINTENANCE-STABILITY")

        return optimal
