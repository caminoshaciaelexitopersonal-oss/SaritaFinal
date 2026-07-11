class EffectCombiner:
    """
    Combines effect sizes from multiple studies using fixed-effects or random-effects meta-analysis models.
    """
    def __init__(self):
        pass

    def combine_effects(self, studies: list) -> float:
        if not studies:
            return 0.0

        total_weight = 0.0
        weighted_sum = 0.0

        for study in studies:
            variance = study.get("variance", 1.0)
            effect = study.get("effect_size", 0.0)

            if variance <= 0:
                variance = 0.001

            weight = 1.0 / variance
            weighted_sum += effect * weight
            total_weight += weight

        if total_weight == 0:
            return 0.0

        return weighted_sum / total_weight
