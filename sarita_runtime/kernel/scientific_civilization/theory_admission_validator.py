class TheoryAdmissionValidator:
    def validate_admission(self, theory):
        # Theory must have evidence > 0.7 and no axiom contradictions
        return theory.get("evidence", 0.0) > 0.7 and not theory.get("contradicts_axiom")
