import time

class IdentityTransitionLedger:
    """
    Tracks all evolutionary transitions from an ontological perspective.
    """
    def __init__(self):
        self.transitions = []

    def record_transition(self, transition_data: dict):
        self.transitions.append({"data": transition_data, "time": time.time()})
        print("TRANSITION LEDGER: Recorded ontological state change.")
