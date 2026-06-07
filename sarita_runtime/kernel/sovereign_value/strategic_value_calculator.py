class StrategicValueCalculator:
    """
    Calculates the mathematical value of a strategic goal or path.
    """
    def calculate_value(self, utility: float, cost: float, risk: float):
        # Value = (Utility / Cost) * (1 - Risk)
        if cost <= 0:
            return 0.0
        return (utility / cost) * (1.0 - risk)
