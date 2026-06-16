import hashlib
import json

class PredictionReplayEngine:
    """
    Re-executes predictions to verify deterministic behavior.
    """
    def __init__(self, forecasting_engine):
        self.forecasting_engine = forecasting_engine

    def replay_prediction(self, original_forecast):
        """
        Reconstructs a prediction from its base state and model parameters.
        """
        reproduced = self.forecasting_engine.forecast_multiverse(original_forecast.get("base_state"))
        return reproduced
