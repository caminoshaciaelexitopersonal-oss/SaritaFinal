import random

class ArchitecturalEvolutionEngine:
    """
    Manages the evolution of architectures through selection and pressure.
    Phase 128.4.
    """
    def __init__(self):
        self.selection_history = []

    def evaluate_fitness(self, architecture):
        genome = architecture["genome"]
        # Fitness is a combination of modularity, resilience and recursion
        fitness = (genome["modularity_index"] * 0.3 +
                   genome["mutation_resilience"] * 0.4 +
                   genome["meta_recursion_level"] * 0.3)
        return round(fitness, 4)

    def select_best(self, architectures):
        if not architectures: return None
        ranked = sorted(architectures, key=lambda x: self.evaluate_fitness(x), reverse=True)
        winner = ranked[0]
        self.selection_history.append(winner["identity"]["id"])
        return winner

    def apply_pressure(self, architecture, pressure_val):
        # Pressure forces mutation or extinction
        if pressure_val > 0.8:
            architecture["genome"]["mutation_resilience"] *= 0.9
            return "MUTATION_TRIGGERED"
        return "STABLE"

    def measure_divergence(self, arch_a, arch_b):
        gen_a = arch_a["genome"]
        gen_b = arch_b["genome"]
        diffs = [abs(gen_a[t] - gen_b[t]) for t in gen_a if t != "signature"]
        return sum(diffs) / len(diffs) if diffs else 0.0

    def check_stability(self, architecture):
        # Stability is high if modularity and resilience are balanced
        mod = architecture["genome"]["modularity_index"]
        res = architecture["genome"]["mutation_resilience"]
        return abs(mod - res) < 0.5
