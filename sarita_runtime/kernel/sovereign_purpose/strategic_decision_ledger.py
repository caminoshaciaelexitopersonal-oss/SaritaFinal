class StrategicDecisionLedger:
    """
    Ledger for decisions made by the Sovereign Strategy Council.
    """
    def __init__(self):
        self.decisions = []

    def record_decision(self, decision: dict):
        self.decisions.append(decision)
        print("STRATEGIC LEDGER: Recorded council decision")
