from sarita_runtime.kernel.adaptive_evolution.constitutional_survival_forecaster import ConstitutionalSurvivalForecaster

def test_future_projection_forgery_attack():
    """
    Attack: Forging a high survival probability for a weak constitution.
    """
    forecaster = ConstitutionalSurvivalForecaster()

    # Weak constitution with very low final fitness
    weak_results = [{"id": "WEAK", "final_fitness": 0.1}]

    forecasts = forecaster.forecast_survival(weak_results)

    # Verification: Forecaster must mark it as EXTINCT_RISK
    assert forecasts[0]["status"] == "EXTINCT_RISK", "Attack failed: Survival forgery successful!"
    assert forecasts[0]["survival_probability"] < 0.2
    print("Future projection forgery attack successfully blocked.")

if __name__ == "__main__":
    test_future_projection_forgery_attack()
