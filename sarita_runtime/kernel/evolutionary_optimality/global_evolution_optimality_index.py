import time

class GlobalEvolutionOptimalityIndex:
    """
    Calculates the GEOI on a 0.0000 to 1.0000 scale.
    """
    def __init__(self, calculator, ledger):
        self.calculator = calculator
        self.ledger = ledger

    def calculate_geoi(self, metrics):
        print("[GlobalEvolutionOptimalityIndex] Calculating GEOI...")

        geoi_data = self.calculator.compute_geoi(metrics)

        self.ledger.record_proof(geoi_data)
        return geoi_data
