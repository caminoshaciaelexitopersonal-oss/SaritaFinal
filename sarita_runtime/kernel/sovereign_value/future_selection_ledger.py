import time

class FutureSelectionLedger:
    """
    Records the results of future competition and trajectory selection.
    """
    def __init__(self):
        self.selections = []

    def record_selection(self, dominant_future_id: str, value: float):
        self.selections.append({"future": dominant_future_id, "value": value, "time": time.time()})
        print(f"SELECTION LEDGER: Recorded selection of {dominant_future_id}")
