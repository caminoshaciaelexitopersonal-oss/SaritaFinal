import time

class SelectionDecisionLedger:
    """
    Records evolutionary selection decisions and their justifications.
    """
    def __init__(self):
        self.decisions = []

    def record_selection(self, selected_id: str, justification: str):
        self.decisions.append({"selected": selected_id, "reason": justification, "time": time.time()})
        print(f"SELECTION LEDGER: Recorded selection of {selected_id}")
