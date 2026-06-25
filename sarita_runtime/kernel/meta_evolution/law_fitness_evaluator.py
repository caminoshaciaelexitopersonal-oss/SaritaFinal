class LawFitnessEvaluator:
    def evaluate_fitness(self, laws, universe_performance):
        # laws with higher innovation and lower extinction thresholds might be "fitter"
        # depending on the universe performance (e.g., complexity emergence)
        innovation = laws.get("innovation_velocity", 0.5)
        stability = laws.get("epistemic_stability", 0.5)

        fitness = (innovation * 0.6) + (stability * 0.4) + universe_performance
        return round(max(0.0, min(1.0, fitness)), 4)
