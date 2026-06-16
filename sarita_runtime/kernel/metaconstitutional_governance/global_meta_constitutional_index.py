import time

class GlobalMetaConstitutionalIndex:
    """
    Calculates the Global Meta-Constitutional Index (GMCI).
    """
    def __init__(self, calculator, ledger):
        self.calculator = calculator
        self.ledger = ledger

    def calculate_gmci(self, metrics):
        print("[GlobalMetaConstitutionalIndex] Calculating GMCI...")

        gmci_data = self.calculator.compute(metrics)

        self.ledger.record(gmci_data)
        return gmci_data
