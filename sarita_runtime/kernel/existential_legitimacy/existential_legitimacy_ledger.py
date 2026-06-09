import time

class ExistentialLegitimacyLedger:
    """
    Records the measured legitimacy of SARITA's existence.
    """
    def __init__(self):
        self.entries = []

    def record_legitimacy(self, score: float):
        self.entries.append({"score": score, "time": time.time()})
        print(f"LEGITIMACY LEDGER: Recorded existence legitimacy: {score}")
