class ConfidenceIntervalCalculator:
    """
    Calculates statistical confidence intervals for predictions.
    """
    def calculate_intervals(self, prediction_value, uncertainty_score, confidence_level=0.999):
        """
        Determines Lower and Upper bounds based on uncertainty.
        """
        margin = uncertainty_score * (1.0 + confidence_level)
        return {
            "lower_bound": max(0.0, prediction_value - margin),
            "upper_bound": min(1.0, prediction_value + margin)
        }
