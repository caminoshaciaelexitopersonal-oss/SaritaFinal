class ForecastQualityValidator:
    """
    Validates the overall quality of a forecast based on fidelity metrics.
    """
    def validate_quality(self, fidelity_data):
        """
        Ensures estructural, behavioral, and evolutionary fidelity targets.
        """
        return all(v >= 0.90 for v in fidelity_data.values())
