class LongTermDominanceEngine:
    """
    Evaluates the long-term dominance of constitutions across simulated futures.
    """
    def __init__(self, projection_engine, competition_simulator, survival_forecaster):
        self.projection_engine = projection_engine
        self.competition_simulator = competition_simulator
        self.survival_forecaster = survival_forecaster

    def evaluate_dominance(self, candidates, generations=500):
        # 1. Project candidate trajectories
        trajectories = self.projection_engine.project_trajectories(candidates, generations)

        # 2. Run competition tournament across time
        competition_results = self.competition_simulator.simulate_competition(trajectories)

        # 3. Forecast survival probability at horizon
        forecasts = self.survival_forecaster.forecast_survival(competition_results)

        return {
            "generations": generations,
            "winner": forecasts[0]["id"] if forecasts else None,
            "forecasts": forecasts
        }
