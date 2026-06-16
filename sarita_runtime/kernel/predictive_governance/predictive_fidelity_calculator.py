class PredictiveFidelityCalculator:
    """
    Calculates the Global Predictive Fidelity Index (GPFI) based on Phase 108.11 criteria.
    """
    def calculate_gpfi(self, accuracy, stability, reproducibility, horizon_reliability, uncertainty):
        """
        Formula: GPFI = Accuracy*0.25 + Stability*0.20 + Reproducibility*0.20 + Horizon*0.20 + Uncertainty*0.15
        """
        gpfi = (
            (accuracy * 0.25) +
            (stability * 0.20) +
            (reproducibility * 0.20) +
            (horizon_reliability * 0.20) +
            (uncertainty * 0.15)
        )
        return min(1.0, max(0.0, gpfi))
