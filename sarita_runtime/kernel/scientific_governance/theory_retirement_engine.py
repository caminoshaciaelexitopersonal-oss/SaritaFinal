class TheoryRetirementEngine:
    def evaluate_retirement(self, theory):
        # Retires theory if it has been obsolete for too long
        if theory.get("lifecycle_state") == "OBSOLESCENCE" and theory.get("obsolescence_duration", 0) > 500:
            return True
        return False
