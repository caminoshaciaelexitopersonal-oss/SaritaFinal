import time

class GlobalEpistemicMaturityIndex:
    """
    Calculates the GEMI on a 0.0000 to 1.0000 scale.
    """
    def __init__(self, calculator, ledger):
        self.calculator = calculator
        self.ledger = ledger

    def calculate_gemi(self, metrics):
        print("[GlobalEpistemicMaturityIndex] Calculating GEMI...")

        gemi_data = self.calculator.compute_gemi(metrics)

        self.ledger.record_event("GEMI_CALCULATION", gemi_data)
        return gemi_data
