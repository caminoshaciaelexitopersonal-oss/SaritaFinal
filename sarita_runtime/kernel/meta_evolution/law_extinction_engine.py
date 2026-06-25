class LawExtinctionEngine:
    def __init__(self):
        self.extinct_laws = []

    def record_extinction(self, laws, reason):
        self.extinct_laws.append({"laws": laws, "reason": reason})

    def get_extinction_count(self):
        return len(self.extinct_laws)
