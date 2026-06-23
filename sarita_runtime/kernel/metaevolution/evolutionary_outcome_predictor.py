class EvolutionaryOutcomePredictor:
    """
    Predicts the long-term outcome based on simulation data.
    """
    def predict_long_term_outcome(self, simulation_data):
        avg_fitness = sum([d["fitness"] for d in simulation_data]) / len(simulation_data)
        if avg_fitness > 0.8:
            return "STABLE_EVOLUTION_ASCENDANCY"
        elif avg_fitness > 0.5:
            return "EQUILIBRIUM_PERSISTENCE"
        else:
            return "DEVOLUTIONARY_RISK"
