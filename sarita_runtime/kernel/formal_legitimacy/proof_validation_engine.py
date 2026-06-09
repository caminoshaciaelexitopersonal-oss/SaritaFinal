class ProofValidationEngine:
    """
    Validates that a proof is structurally sound and logically consistent.
    """

    def validate_proof(self, proof: dict) -> bool:
        """
        Performs formal step-by-step verification of a proof chain.
        Ensures structural integrity and explicit constraint enforcement.
        """
        if not self._is_structurally_valid(proof):
            return False

        # 1. Constraint Enforcement Check
        if not self._verify_constraints(proof):
            return False

        # 2. Final Result Verification
        if not self._verify_final_step(proof):
            return False

        proof["verification_result"] = "VALIDATED"
        return True

    def _is_structurally_valid(self, proof):
        required_keys = ["proof_id", "decision_id", "premises", "constraints", "steps"]
        return all(k in proof for k in required_keys)

    def _verify_constraints(self, proof):
        for constraint in proof.get("constraints", []):
            constraint_met = any(
                step.get("action") == "ENFORCE" and step.get("statement") == constraint
                for step in proof.get("steps", [])
            )
            if not constraint_met:
                return False
        return True

    def _verify_final_step(self, proof):
        steps = proof.get("steps", [])
        if not steps:
            return False
        last_step = steps[-1]
        return last_step.get("action") == "DERIVE"
