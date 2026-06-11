import math

class ForecastErrorAnalyzer:
    """
    Performs formal error analysis (MAE, RMSE, MAPE) on forecasts.
    """
    def analyze_errors(self, deviations):
        """
        Calculates error metrics from a dictionary of deviations.
        """
        if not deviations:
            return {"mae": 1.0, "rmse": 1.0, "mape": 1.0}

        vals = list(deviations.values())
        mae = sum(vals) / len(vals)
        rmse = math.sqrt(sum(v**2 for v in vals) / len(vals))
        mape = (sum(vals) / sum(deviations.keys())) if sum(deviations.keys()) > 0 else mae # Simplified MAPE proxy

        return {
            "mae": mae,
            "rmse": rmse,
            "mape": mape
        }
