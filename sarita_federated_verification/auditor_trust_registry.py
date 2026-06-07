class AuditorTrustRegistry:
    """
    Tracks the trust level and reputation of federated auditors based on historical performance.
    """
    def __init__(self):
        self.trust_scores = {} # auditor_id -> score

    def update_trust(self, auditor_id: str, success: bool):
        current_score = self.trust_scores.get(auditor_id, 1.0)
        if success:
            self.trust_scores[auditor_id] = min(current_score + 0.1, 5.0)
        else:
            self.trust_scores[auditor_id] = max(current_score - 1.0, 0.0)

    def is_trusted(self, auditor_id: str, threshold: float = 1.0):
        return self.trust_scores.get(auditor_id, 1.0) >= threshold
