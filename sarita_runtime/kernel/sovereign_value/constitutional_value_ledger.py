import time

class ConstitutionalValueLedger:
    """
    Records the measured value of constitutional objectives over time.
    """
    def __init__(self):
        self.entries = []

    def record_value(self, goal_id: str, value: float):
        entry = {"goal": goal_id, "value": value, "time": time.time()}
        self.entries.append(entry)
        print(f"VALUE LEDGER: Recorded {goal_id} value: {value}")
