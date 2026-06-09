import uuid
import time

class FormalProofEngine:
    """
    Orchestrates the generation and validation of formal proofs for SARITA decisions.
    """
    def __init__(self, generator, validator, registry):
        self.generator = generator
        self.validator = validator
        self.registry = registry

    def prove_decision(self, decision_id: str, premises: list, constraints: list, logic_type: str = "PROPOSITIONAL"):
        """
        Generates a formal proof for a given decision.
        """
        proof = self.generator.generate_proof(decision_id, premises, constraints, logic_type)
        is_valid = self.validator.validate_proof(proof)

        if is_valid:
            self.registry.register_theorem(proof)

        return proof if is_valid else None
