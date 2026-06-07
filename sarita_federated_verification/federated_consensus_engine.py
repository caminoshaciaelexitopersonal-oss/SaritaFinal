import hashlib
import time

class FederatedConsensusEngine:
    """
    Manages consensus across multiple independent organizational domains.
    """
    def __init__(self, min_domains: int = 3):
        self.min_domains = min_domains
        self.domain_verdicts = {} # evidence_hash -> {domain_id: verdict}

    def submit_domain_verdict(self, evidence_hash: str, domain_id: str, verdict: bool):
        if evidence_hash not in self.domain_verdicts:
            self.domain_verdicts[evidence_hash] = {}
        self.domain_verdicts[evidence_hash][domain_id] = verdict

    def validate_federated_quorum(self, evidence_hash: str):
        verdicts = self.domain_verdicts.get(evidence_hash, {})
        if len(verdicts) < self.min_domains:
            return False, f"Insufficient domain diversity ({len(verdicts)}/{self.min_domains})"

        positive_domains = [d for d, v in verdicts.items() if v is True]
        if len(positive_domains) >= self.min_domains:
            return True, "Federated consensus reached across independent domains."
        return False, "Federated quorum not met."
