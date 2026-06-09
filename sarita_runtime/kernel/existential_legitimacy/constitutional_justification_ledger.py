import time

class ConstitutionalJustificationLedger:
    """
    Tracks the historical justifications and net benefit of existence.
    """
    def __init__(self):
        self.entries = []

    def record_justification(self, net_legitimacy: float):
        self.entries.append({"net": net_legitimacy, "time": time.time()})
        print(f"JUSTIFICATION LEDGER: Recorded net benefit: {net_legitimacy}")
