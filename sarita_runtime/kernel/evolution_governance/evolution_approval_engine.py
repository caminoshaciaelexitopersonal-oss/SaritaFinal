import time

class EvolutionApprovalEngine:
    """
    Proposed -> Evaluated -> Simulated -> Certified -> Approved.
    """
    def __init__(self, approval_validator, consensus_builder, certifier, ledger):
        self.approval_validator = approval_validator
        self.consensus_builder = consensus_builder
        self.certifier = certifier
        self.ledger = ledger

    def process_approval(self, proposal, evaluation_res, simulation_res):
        print(f"[EvolutionApprovalEngine] Processing approval for {proposal.get('id')}...")

        consensus = self.consensus_builder.build_consensus(proposal)
        is_certified = self.certifier.certify_evolution(proposal, evaluation_res, simulation_res)
        valid = self.approval_validator.validate_approval(consensus, is_certified)

        result = {
            "proposal_id": proposal.get("id"),
            "consensus_reached": consensus["reached"],
            "is_certified": is_certified,
            "approved": valid,
            "timestamp": time.time()
        }

        self.ledger.record(result)
        return result
