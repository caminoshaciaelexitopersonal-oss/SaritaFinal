class EvolutionCertifier:
    """Certifies evolutionary proposals based on combined evidence from evaluation and simulation."""
    def certify_evolution(self, proposal, evaluation_res, simulation_res):
        # Multi-factor certification
        is_legal = evaluation_res.get("is_approved", False)
        stability = simulation_res.get("global_stability_index", 0.0)

        # Proposal-specific evidence check
        has_id = len(proposal.get("id", "")) > 0

        return is_legal and stability > 0.85 and has_id
