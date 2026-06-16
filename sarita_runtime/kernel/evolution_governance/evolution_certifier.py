class EvolutionCertifier:
    """Certifies evolutionary proposals based on evaluation and simulation results."""
    def certify_evolution(self, proposal, evaluation_res, simulation_res):
        return evaluation_res.get("is_approved") and simulation_res.get("global_stability_index") > 0.9
