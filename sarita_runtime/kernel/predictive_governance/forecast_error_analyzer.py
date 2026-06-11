class ForecastErrorAnalyzer:
    """
    Analyzes the error between predictions and actual outcomes.
    """
    def analyze_error(self, prediction, actual):
        """
        Calculates Root Mean Square Error (RMSE) for numerical projections.
        """
        if not isinstance(prediction, dict) or not isinstance(actual, dict):
            return 1.0

        common_keys = [k for k in prediction if k in actual and isinstance(prediction[k], (int, float))]
        if not common_keys:
            return 1.0

        squared_errors = [(prediction[k] - actual[k])**2 for k in common_keys]
        rmse = math.sqrt(sum(squared_errors) / len(common_keys))

        return min(1.0, rmse)

import math
