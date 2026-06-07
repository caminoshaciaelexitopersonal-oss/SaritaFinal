class EvidenceReplayCertifier:
    """
    Certifies that evidence produced by one instance can be deterministically
    replayed and verified by a separate, reference implementation.
    """
    @staticmethod
    def certify_replay(original_verdict: bool, reference_verdict: bool):
        if original_verdict == reference_verdict:
            return True, "Replay certification successful: Implementations converged."
        return False, "Replay certification failed: Implementations diverged."
