class TheoremDerivationEngine:
    """
    Handles the derivation of theorems using the inference engine.
    """
    def __init__(self, reasoner):
        self.reasoner = reasoner

    def derive_theorem(self, knowledge, conclusion):
        chain = self.reasoner.derive(knowledge, conclusion)
        if not chain:
            return None

        return {
            "inference_chain": chain,
            "conclusion": str(conclusion),
            "proof_length": len(chain)
        }
