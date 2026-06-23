import time

class GlobalEpistemicCompletenessIndex:
    """
    Calculates the GECI on a 0.0000 to 1.0000 scale.
    """
    def __init__(self, calculator, ledger):
        self.calculator = calculator
        self.ledger = ledger

    def calculate_geci(self, metrics):
        print("[GlobalEpistemicCompletenessIndex] Calculating GECI...")

        geci_data = self.calculator.compute_geci(metrics)

        self.ledger.record_bound(geci_data)
        return geci_data
