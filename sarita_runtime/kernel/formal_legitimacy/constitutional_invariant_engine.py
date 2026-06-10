class ConstitutionalInvariantEngine:
    """
    Ensures that no reform or decision breaks the system's core invariants.
    """
    def __init__(self, validators: list):
        self.validators = validators

    def verify_invariants(self, proposed_state: dict) -> dict:
        results = {}
        all_passed = True

        for validator in self.validators:
            is_valid, reason = validator.validate(proposed_state)
            results[validator.__class__.__name__] = {
                "is_valid": is_valid,
                "reason": reason
            }
            if not is_valid:
                all_passed = False

        return {
            "all_passed": all_passed,
            "validation_results": results
        }
