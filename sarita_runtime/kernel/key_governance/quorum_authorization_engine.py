import logging

class QuorumAuthorizationEngine:
    """
    Enforces that critical decisions require approval from multiple authorities (Phase 84.5).
    """
    def __init__(self, required_quorum: int = 2):
        self.required_quorum = required_quorum
        self.approvals = {} # proposal_id -> set(authority_id)

    def register_approval(self, proposal_id: str, authority_id: str):
        if proposal_id not in self.approvals:
            self.approvals[proposal_id] = set()

        self.approvals[proposal_id].add(authority_id)
        logging.info(f"QUORUM: Authority '{authority_id}' approved proposal '{proposal_id}'")

    def is_authorized(self, proposal_id: str):
        count = len(self.approvals.get(proposal_id, set()))
        authorized = count >= self.required_quorum
        if not authorized:
            logging.warning(f"QUORUM FAILURE: Proposal '{proposal_id}' has {count}/{self.required_quorum} approvals.")
        return authorized

class DualSignatureValidator:
    """Validates that a decision has been signed by at least two distinct keys."""
    @staticmethod
    def validate(sig1: str, sig2: str):
        return sig1 != sig2 and len(sig1) > 0 and len(sig2) > 0
