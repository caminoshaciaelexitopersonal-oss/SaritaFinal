import hashlib
import time

class AuditorConsensusEngine:
    """
    Coordinates consensus between multiple independent auditors (Phase 87.4).
    """
    def __init__(self, required_quorum: int = 3):
        self.required_quorum = required_quorum
        self.verdicts = {} # evidence_hash -> list of verdicts

    def submit_verdict(self, auditor_id: str, evidence_hash: str, verdict: bool, signature: str):
        if evidence_hash not in self.verdicts:
            self.verdicts[evidence_hash] = []

        self.verdicts[evidence_hash].append({
            "auditor": auditor_id,
            "verdict": verdict,
            "signature": signature,
            "timestamp": time.time()
        })

    def get_consensus(self, evidence_hash: str):
        audit_list = self.verdicts.get(evidence_hash, [])
        positive_verdicts = [v for v in audit_list if v["verdict"] is True]

        if len(positive_verdicts) >= self.required_quorum:
            return True, "Consensus reached."
        return False, f"Quorum not met ({len(positive_verdicts)}/{self.required_quorum})"

class ConsensusCertificate:
    """Certified proof of multi-auditor consensus."""
    def __init__(self, evidence_hash: str, auditors: list):
        self.evidence_hash = evidence_hash
        self.auditors = auditors
        self.certified_at = time.time()
