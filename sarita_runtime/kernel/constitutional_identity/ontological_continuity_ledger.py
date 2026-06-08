import time

class OntologicalContinuityLedger:
    """
    The absolute record of SARITA's continuity as the same entity.
    """
    def __init__(self):
        self.records = []

    def record_continuity(self, verdict: str, score: float):
        self.records.append({"verdict": verdict, "score": score, "time": time.time()})
        print(f"CONTINUITY LEDGER: Recorded {verdict} with score {score}.")
