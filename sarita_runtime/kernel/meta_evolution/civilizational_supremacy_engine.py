class CivilizationalSupremacyEngine:
    """
    Calculates and validates Global Civilizational Supremacy.
    """
    def __init__(self, score_calculator, horizon_comparator, dominance_validator):
        self.score_calculator = score_calculator
        self.horizon_comparator = horizon_comparator
        self.dominance_validator = dominance_validator

    def certify_supremacy(self, target_civilization, competitors):
        # 1. Calculate GCSI
        gcsi = self.score_calculator.calculate_gcsi(target_civilization)

        # 2. Compare over long horizons
        dominance_ratio = self.horizon_comparator.compare_horizons(target_civilization, competitors)

        # 3. Validate global dominance
        is_dominant = self.dominance_validator.validate_dominance(target_civilization, competitors)

        return {
            "gcsi": gcsi,
            "dominance_ratio": dominance_ratio,
            "is_dominant": is_dominant,
            "certified": gcsi > 0.95 and is_dominant
        }
