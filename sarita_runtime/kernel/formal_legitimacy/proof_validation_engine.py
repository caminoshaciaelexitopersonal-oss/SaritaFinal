class ProofValidationEngine:
    """
    Validates that a proof is structurally sound and logically consistent.
    """

    def validate_proof(self, proof: dict) -> bool:
        if not proof or "steps" not in proof:
            return False

        # 1. Structural Validation
        required_keys = ["proof_id", "decision_id", "premises", "constraints", "steps"]
        if not all(k in proof for k in required_keys):
            return False

        # 2. Logical Consistency and Constraint Enforcement
        # Every constraint MUST be explicitly mentioned and enforced in the proof steps.
        for constraint in proof.get("constraints", []):
            constraint_met = any(
                step.get("action") == "ENFORCE" and step.get("statement") == constraint
                for step in proof["steps"]
            )
            if not constraint_met:
                # If a constraint is not explicitly enforced, the proof is invalid.
                return False

        # 3. Final Result Verification
        last_step = proof["steps"][-1]
        if last_step.get("action") != "DERIVE":
            return False

        proof["verification_result"] = "VALIDATED"
        return True
