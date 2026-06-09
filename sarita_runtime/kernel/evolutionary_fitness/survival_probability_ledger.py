import time

class SurvivalProbabilityLedger:
    """
    Tracks the historical survival probability (P_s).
    """
    def __init__(self):
        self.entries = []

    def record_p_s(self, p_s: float):
        self.entries.append({"p_s": p_s, "time": time.time()})
        print(f"SURVIVAL PROB LEDGER: Recorded P_s: {p_s}")
