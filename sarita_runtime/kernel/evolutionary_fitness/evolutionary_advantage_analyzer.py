class EvolutionaryAdvantageAnalyzer:
    """
    Analyzes the "Evolutionary Advantage" (E_a) of one trajectory over another.
    """
    def analyze_advantage(self, fitness_a: float, fitness_b: float):
        if fitness_b <= 0:
            return 1.0 if fitness_a > 0 else 0.0
        return fitness_a / fitness_b
