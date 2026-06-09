import time

class CivilizationalAlignmentLedger:
    """
    Records all alignment checks and scores back to Phase 1.
    """
    def __init__(self):
        self.entries = []

    def record_alignment(self, score: float):
        self.entries.append({"score": score, "time": time.time()})
        print(f"ALIGNMENT LEDGER: Recorded scorecard value: {score}")
