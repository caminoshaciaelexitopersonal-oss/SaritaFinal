class ArchitectureChangeProposal:
    """Data model for architectural change proposals (Phase 81.4)."""
    def __init__(self, proposal_id, details):
        self.proposal_id = proposal_id
        self.details = details
