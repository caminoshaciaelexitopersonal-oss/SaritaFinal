class IrreversibleLossTracker:
    def __init__(self):
        self.extinct_civs = []

    def record_extinction(self, civ, reason):
        self.extinct_civs.append({
            "civ_id": civ["identity"]["id"],
            "name": civ["identity"]["name"],
            "reason": reason,
            "final_age": civ.get("age", 0)
        })

    def get_extinction_count(self):
        return len(self.extinct_civs)
