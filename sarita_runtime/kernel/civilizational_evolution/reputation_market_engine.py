class ReputationMarketEngine:
    def update_reputation(self, institution, performance):
        current = institution.get("reputation", 1.0)
        institution["reputation"] = max(0.1, min(5.0, current + performance))
