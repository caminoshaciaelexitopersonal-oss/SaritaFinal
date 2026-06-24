class InstitutionExtinctionEngine:
    def check_extinction(self, institution):
        if institution["resources"] < 0.05 or institution["fitness"] < 0.1:
            institution["status"] = "EXTINCT"
            return True
        return False
