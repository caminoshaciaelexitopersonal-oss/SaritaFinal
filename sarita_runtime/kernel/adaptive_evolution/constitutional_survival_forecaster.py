class ConstitutionalSurvivalForecaster:
    """
    Forecasts the survival probability of constitutions at a given horizon.
    """
    def forecast_survival(self, competition_results):
        forecasts = []
        for r in competition_results:
            # Survival prob linked to final fitness
            prob = max(0.0, min(1.0, r["final_fitness"] * 1.05))
            forecasts.append({
                "id": r["id"],
                "survival_probability": float(round(prob, 4)),
                "status": "DOMINANT" if prob > 0.9 else "EXTINCT_RISK"
            })
        return forecasts
