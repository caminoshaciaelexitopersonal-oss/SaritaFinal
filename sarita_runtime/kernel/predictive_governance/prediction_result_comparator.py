class PredictionResultComparator:
    """
    Compares predicted governance states against observed results.
    """
    def compare(self, prediction, actual):
        """
        Calculates deviations across key governance metrics.
        """
        keys = set(prediction.keys()) & set(actual.keys())
        deviations = {k: abs(prediction[k] - actual[k]) for k in keys if isinstance(prediction[k], (int, float))}
        return deviations
