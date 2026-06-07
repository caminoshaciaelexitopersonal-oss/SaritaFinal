class AdaptiveMaturityCalculator:
    """
    Calculates the adaptive maturity level of the system.
    """
    def calculate_maturity(self, accuracy: float, success_rate: float, learning_velocity: float):
        # Weighted average of maturity factors
        maturity = (accuracy * 0.4) + (success_rate * 0.4) + (learning_velocity * 0.2)
        return maturity
