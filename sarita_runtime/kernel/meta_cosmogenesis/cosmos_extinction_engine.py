import time

class CosmosExtinctionEngine:
    """
    Manages the graceful or catastrophic extinction of cosmos based on fitness or selection.
    """
    def __init__(self):
        self.extinction_ledger = []

    def execute_extinction(self, cosmos, reason="LOW_FITNESS"):
        cosmos["status"] = "EXTINCT"
        cosmos["extinguished_at"] = time.time()

        entry = {
            "cosmos_id": cosmos["identity"]["id"],
            "timestamp": cosmos["extinguished_at"],
            "reason": reason,
            "age": cosmos["age"]
        }
        self.extinction_ledger.append(entry)
        return entry

    def is_viable(self, cosmos):
        # Basic viability: no trait should be exactly 0
        for trait, value in cosmos["genome"].items():
            if trait == "signature": continue
            if value <= 0: return False
        return True
