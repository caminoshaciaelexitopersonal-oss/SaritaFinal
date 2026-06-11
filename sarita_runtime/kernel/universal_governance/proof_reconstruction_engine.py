class ProofReconstructionEngine:
    """
    Reconstructs the full mathematical proof chain for a theorem.
    """
    def reconstruct_proof(self, theorem):
        """
        Reconstructs the path: Axiom -> Hypothesis -> Experiment -> Law -> Theorem
        """
        # Prohibited: uuid_only_proofs
        proof_chain = {
            "theorem_id": theorem.id,
            "axiom": theorem.source_axiom,
            "hypothesis": theorem.hypothesis,
            "experiment": theorem.experiment_id,
            "law": theorem.source_law_id,
            "inference_steps": theorem.inference_steps,
            "conclusion": theorem.expression
        }
        return proof_chain
