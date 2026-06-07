import time

class ConstitutionalChangeRegistry:
    """
    Maintains an immutable record of all applied constitutional changes.
    """
    def __init__(self):
        self.changes = []

    def register_change(self, proposal):
        self.changes.append({
            "proposal": proposal,
            "applied_at": time.time(),
            "status": "APPLIED"
        })
