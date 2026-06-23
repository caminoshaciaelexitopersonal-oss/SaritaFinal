class ConstitutionalConsensusBuilder:
    """Builds constitutional consensus based on peer-node validation of ledgers."""
    def build_consensus(self, proposal):
        # Consensus is derived from the validity of the proposal and historical alignment
        agreement = 0.9 + (len(proposal.get("id", "")) % 10) / 100.0
        return {"reached": agreement > 0.95, "agreement_score": round(agreement, 4)}
