class ExistentialLegitimacyEngine:
    """
    The engine that justifies SARITA's existence.
    """
    def __init__(self, registry, calculator, validator):
        self.registry = registry
        self.calculator = calculator
        self.validator = validator

    def assess_existential_legitimacy(self, metrics: dict):
        justifications = self.registry.get_validated_justifications()
        valid_ratio = self.validator.validate_existence(justifications, metrics)
        score = self.calculator.calculate_l_e(valid_ratio, 0.1, 0.95) # Baseline cost 0.1, necessity 0.95

        return {
            "legitimacy_score": score,
            "validation_ratio": valid_ratio,
            "timestamp": time.time(),
            "verdict": "LEGITIMATE" if score > 1.0 else "UNJUSTIFIED"
        }
