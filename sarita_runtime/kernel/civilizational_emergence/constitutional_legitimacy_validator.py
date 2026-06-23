class ConstitutionalLegitimacyValidator:
    def validate_legitimacy(self, constitution):
        # Legitimacy is based on support from active institutions
        return constitution.get("legitimacy", 0.5) > 0.7
