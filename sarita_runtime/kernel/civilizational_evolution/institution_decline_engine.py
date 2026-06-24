class InstitutionDeclineEngine:
    def decline(self, institution):
        institution["resources"] *= 0.9
        institution["fitness"] -= 0.02
        institution["status"] = "DECLINE"
        return institution
