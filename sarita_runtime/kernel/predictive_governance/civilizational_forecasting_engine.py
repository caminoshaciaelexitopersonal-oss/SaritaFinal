class CivilizationalForecastingEngine:
    """
    Main engine for civilizational forecasting and long-term projection.
    """
    def __init__(self, builder, predictor, validator, ledger):
        self.builder = builder
        self.predictor = predictor
        self.validator = validator
        self.ledger = ledger

    def forecast_civilization(self, current_params, target_horizons=[10, 50, 100, 500, 1000], simulations_per_horizon=20000):
        """
        Generates 100,000 civilizational projections (target_horizons * simulations_per_horizon).
        """
        all_forecasts = []

        for gen in target_horizons:
            horizon_forecasts = []
            for i in range(simulations_per_horizon):
                # Add slight variance to each simulation for statistical depth
                varied_params = {k: v * (0.95 + 0.1 * (i / simulations_per_horizon)) for k, v in current_params.items()}

                projected = self.builder.build_future_civilization(varied_params, gen)
                is_valid = self.validator.validate_projection(varied_params, projected, gen)
                survival_prob = self.predictor.predict_long_horizon(projected, gen)

                horizon_forecasts.append({
                    "id": f"SIM-{gen}-{i}",
                    "projected": projected,
                    "survival_prob": survival_prob,
                    "is_valid": is_valid
                })

            # Aggregate horizon results to save memory while preserving auditability
            aggregated = self._aggregate_forecasts(gen, horizon_forecasts)
            all_forecasts.append(aggregated)

        if self.ledger:
            self.ledger.record_prediction("CIVILIZATIONAL_MASSIVE", all_forecasts)

        return all_forecasts

    def _aggregate_forecasts(self, horizon, forecasts):
        avg_survival = sum(f["survival_prob"] for f in forecasts) / len(forecasts)
        return {
            "horizon": horizon,
            "sample_size": len(forecasts),
            "mean_survival_probability": avg_survival,
            "validation_rate": sum(1 for f in forecasts if f["is_valid"]) / len(forecasts)
        }
