class MetaConsensusPoisoningAttack:
    """
    Simulates multiple consensuses that agree on a false verdict but are derived from the same implementation.
    """
    def run_attack(self, meta_engine, v_ids):
        # Even if verdicts agree, IDS check should catch it if v_ids lack diversity
        meta_engine.register_consensus("c1", True, v_ids)
        success, msg = meta_engine.validate_meta_consensus()
        if not success and "Diversity" in msg:
            return True, "Attack blocked: Meta-consensus poisoned with low-diversity verifiers."
        return False, "Attack succeeded: Poisoned consensus accepted."
