import random

class ConstraintSystemGenerator:
    """
    Generates universal constraints (e.g., speed of light equivalent, entropy bounds).
    """
    def generate_constraints(self, genome):
        return {
            "information_bottleneck": round(genome.get("causality_linearity", 0.5) * random.uniform(0.8, 1.2), 4),
            "entropy_max": round(genome.get("logical_entropy", 0.5) * 1000, 2),
            "complexity_limit": round(random.uniform(10**6, 10**12), 0)
        }
