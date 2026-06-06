class MetaConsensusEngine:
    """
    Validates the legitimacy of consensus by evaluating multiple independent consensus results.
    """
    def __init__(self, ids_engine):
        self.ids_engine = ids_engine
        self.consensuses = {} # consensus_id -> {verdict, verifiers}

    def register_consensus(self, consensus_id: str, verdict: bool, verifier_ids: list):
        self.consensuses[consensus_id] = {
            "verdict": verdict,
            "verifiers": verifier_ids
        }

    def validate_meta_consensus(self):
        if not self.consensuses:
            return False, "No consensus results registered."

        # All consensuses must agree
        verdicts = [c["verdict"] for c in self.consensuses.values()]
        if not all(v == verdicts[0] for v in verdicts):
            return False, "Consensus divergence detected at meta-level!"

        # Verify aggregate diversity across all verifiers involved
        all_verifiers = set()
        for c in self.consensuses.values():
            all_verifiers.update(c["verifiers"])

        ids = self.ids_engine.calculate_ids(list(all_verifiers))
        if ids < 0.70:
            return False, f"Meta-consensus rejected: Low Diversity Score ({ids:.2f} < 0.70)"

        return True, f"Meta-consensus reached with IDS {ids:.2f}"
