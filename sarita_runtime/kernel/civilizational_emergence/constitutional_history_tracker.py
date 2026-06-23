class ConstitutionalHistoryTracker:
    def __init__(self):
        self.history = []

    def record_revision(self, constitution_id, amendment):
        self.history.append({"id": constitution_id, "amendment": amendment})

    def get_history(self):
        return self.history
