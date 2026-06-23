import time

class GlobalConstitutionalEvolutionIndex:
    """
    Calculates the Global Constitutional Evolution Index (GCEI).
    """
    def __init__(self, calculator, ledger):
        self.calculator = calculator
        self.ledger = ledger

    def calculate_gcei(self, metrics):
        print("[GlobalConstitutionalEvolutionIndex] Calculating GCEI...")

        gcei_data = self.calculator.compute(metrics)

        self.ledger.record(gcei_data)
        return gcei_data
