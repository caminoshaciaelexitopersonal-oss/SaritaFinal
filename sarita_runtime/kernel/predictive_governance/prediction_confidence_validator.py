class PredictionConfidenceValidator:
    """
    Validates the statistical confidence of a prediction.
    """
    def validate_confidence(self, prediction_data):
        """
        Calculates confidence based on data variance and sample size.
        """
        variance = prediction_data.get("variance", 0.0)
        sample_size = prediction_data.get("sample_size", 1)

        if sample_size <= 0:
            return 0.0

        # Confidence increases with sample size and decreases with variance
        confidence = (1.0 - variance) * (1.0 - (1.0 / math.log(sample_size + 1)))
        return min(1.0, max(0.0, confidence))

import math
