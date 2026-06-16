import math

class LongHorizonPredictor:
    """
    Predicts outcomes for long horizons (1000+ generations).
    """
    def predict_long_horizon(self, civilization, generations=1000):
        """
        Calculates survival probability using a multi-factor decay model.
        """
        legitimacy = civilization.get("legitimacy", 1.0)
        stability = civilization.get("stability", 1.0)
        adaptation = civilization.get("adaptation", 1.0)

        # Base decay rate modified by adaptation
        base_decay = 0.0001 * (1.0 - adaptation)

        # Survival prob = (L * S) * e^(-decay * generations)
        survival_prob = (legitimacy * stability) * math.exp(-base_decay * generations)

        return min(1.0, max(0.0, survival_prob))
