class ParadigmTransitionValidator:
    def validate(self, old_paradigm, new_paradigm, verification_data):
        # Ensures transition doesn't break constitutional invariants
        if new_paradigm.get("explains_anomalies") and verification_data.get("invariant_check"):
            return True
        return False
