import time

class FoundationalDecisionLedger:
    """
    Ledger for high-level foundational decisions that impact civilizational alignment.
    """
    def __init__(self):
        self.decisions = []

    def record_foundational_decision(self, decision: dict):
        self.decisions.append({"decision": decision, "time": time.time()})
        print("FOUNDATIONAL LEDGER: Recorded oversight council decision.")
