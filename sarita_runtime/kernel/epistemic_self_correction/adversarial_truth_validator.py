class AdversarialTruthValidator:
    def validate_resistance(self, truth_claim, attacks):
        # Measures how well a truth claim survives contradictory evidence
        survived = sum(1 for a in attacks if not a.get("successful"))
        return survived / len(attacks) if attacks else 1.0
