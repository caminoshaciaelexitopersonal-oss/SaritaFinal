class EssenceDegradationAnalyzer:
    """
    Analyzes the gradual degradation of the constitutional essence.
    """
    def analyze_degradation(self, generations: int, mutation_rate: float):
        # Essence degrades over time if mutations are allowed in the core.
        final_essence = 1.0 * ((1.0 - mutation_rate) ** generations)
        return final_essence
