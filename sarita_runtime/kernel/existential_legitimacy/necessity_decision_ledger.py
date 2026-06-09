import time

class NecessityDecisionLedger:
    """
    Records decisions related to constitutional necessity and criticality.
    """
    def __init__(self):
        self.decisions = []

    def record_necessity(self, score: float):
        self.decisions.append({"necessity": score, "time": time.time()})
        print(f"NECESSITY LEDGER: Recorded necessity score: {score}")
