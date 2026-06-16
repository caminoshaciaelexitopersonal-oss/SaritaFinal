class GlobalPredictiveFidelityIndex:
    """
    Main engine for the Global Predictive Fidelity Index (GPFI).
    Scale: 0.0000 -> 1.0000
    """
    def __init__(self, calculator, ledger):
        self.calculator = calculator
        self.ledger = ledger

    def certify_gpfi(self, components):
        """
        Calculates and certifies the GPFI using verified evidence.
        """
        gpfi_value = self.calculator.calculate_gpfi(
            components.get("accuracy", 0.0),
            components.get("stability", 0.0),
            components.get("reproducibility", 0.0),
            components.get("horizon_reliability", 0.0),
            components.get("uncertainty_calibration", 0.0)
        )

        certification = {
            "gpfi_score": gpfi_value,
            "components": components,
            "timestamp": "2024-06-11T16:00:00Z",
            "status": "CERTIFIED" if gpfi_value >= 0.90 else "INSUFFICIENT"
        }

        if self.ledger:
            self.ledger.record_gpfi_certification(certification)

        return certification
