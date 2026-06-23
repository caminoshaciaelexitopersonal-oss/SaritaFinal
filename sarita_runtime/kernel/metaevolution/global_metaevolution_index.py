import time

class GlobalMetaevolutionIndex:
    """
    Calculates the Global Metaevolution Index (GMEI) on a 0.0000 to 1.0000 scale.
    """
    def __init__(self, calculator, ledger):
        self.calculator = calculator
        self.ledger = ledger

    def calculate_gmei(self, metrics):
        print("[GlobalMetaevolutionIndex] Calculating GMEI...")

        gmei_data = self.calculator.compute(metrics)

        self.ledger.record_event("GMEI_CALCULATION", gmei_data)
        return gmei_data
