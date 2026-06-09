class ResilienceMeasurementEngine:
    """
    Quantifies the resilience of a constitution under specific stress.
    """
    def measure_impact(self, constitution, scenario):
        # Impact depends on scenario severity and current constitutional fitness
        # In a real system, this involves simulating system degradation.
        return scenario["severity"] * 0.5
