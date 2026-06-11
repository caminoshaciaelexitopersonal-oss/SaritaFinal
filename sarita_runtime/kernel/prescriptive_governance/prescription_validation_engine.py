class PrescriptionValidationEngine:
    """
    Main engine for validating governance prescriptions in Phase 109.11.
    """
    def __init__(self, verifier, feasibility_checker, consistency_validator, ledger):
        self.verifier = verifier
        self.feasibility_checker = feasibility_checker
        self.consistency_validator = consistency_validator
        self.ledger = ledger

    def validate_and_certify(self, prescription):
        """
        Performs full scientific validation of a recommendation.
        """
        is_verified, v_msg = self.verifier.verify_prescription(prescription)
        is_feasible = self.feasibility_checker.check_feasibility(prescription, {})
        is_consistent = self.consistency_validator.validate_consistency([prescription])

        valid = is_verified and is_feasible and is_consistent

        result = {
            "prescription_id": prescription.get("id"),
            "status": "CERTIFIED" if valid else "REJECTED",
            "validation_details": {
                "verified": is_verified,
                "feasible": is_feasible,
                "consistent": is_consistent
            }
        }

        if self.ledger:
            self.ledger.record_validation(result)

        return result
