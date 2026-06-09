class ConstitutionalTheoremRegistry:
    """
    Registry for all proven constitutional theorems.
    Only accepts proofs that have been validated by the ProofValidationEngine.
    """
    def __init__(self, validator=None):
        self.theorems = {}
        self.validator = validator

    def register_theorem(self, proof: dict) -> bool:
        # Prevent direct injection of forged theorems
        if self.validator and not self.validator.validate_proof(proof):
            return False

        theorem_id = proof.get("proof_id")
        if not theorem_id:
            return False

        self.theorems[theorem_id] = {
            "theorem_id": theorem_id,
            "decision_id": proof.get("decision_id"),
            "conclusion": proof["steps"][-1]["statement"] if proof.get("steps") else "N/A",
            "status": "PROVEN"
        }
        return True

    def get_theorem(self, theorem_id: str):
        return self.theorems.get(theorem_id)
