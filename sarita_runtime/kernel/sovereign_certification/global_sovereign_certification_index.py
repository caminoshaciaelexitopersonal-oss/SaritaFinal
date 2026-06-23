import time

class GlobalSovereignCertificationIndex:
    """
    Calculates the GSCI on a 0.0000 to 1.0000 scale.
    """
    def __init__(self, calculator, ledger):
        self.calculator = calculator
        self.ledger = ledger

    def calculate_gsci(self, metrics):
        print("[GlobalSovereignCertificationIndex] Calculating GSCI...")

        gsci_data = self.calculator.compute_gsci(metrics)

        self.ledger.record_certification(gsci_data)
        return gsci_data
