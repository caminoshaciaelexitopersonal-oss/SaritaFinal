import hashlib
import random

class ArchitectureGenomeBuilder:
    """
    Builds the 'genome' of an architecture.
    Defines structural biases, modularity, and evolutionary potential.
    """
    def __init__(self):
        self.traits = [
            "modularity_index", "layer_permeability", "abstraction_depth",
            "redundancy_ratio", "coupling_strength", "governance_strictness",
            "mutation_resilience", "meta_recursion_level"
        ]

    def build_genome(self, parent_genome=None, divergence=0.08):
        if parent_genome:
            return self._mutate_genome(parent_genome, divergence)

        genome = {trait: round(random.uniform(0.1, 1.0), 4) for trait in self.traits}
        genome["signature"] = self._calculate_signature(genome)
        return genome

    def _mutate_genome(self, parent_genome, divergence):
        new_genome = {}
        for trait, value in parent_genome.items():
            if trait == "signature": continue
            mutation = random.uniform(-divergence, divergence)
            new_genome[trait] = round(max(0.0001, min(1.0, value + mutation)), 4)

        new_genome["signature"] = self._calculate_signature(new_genome)
        return new_genome

    def _calculate_signature(self, genome):
        raw = "".join([f"{k}:{v}" for k, v in sorted(genome.items()) if k != "signature"])
        return hashlib.sha384(raw.encode()).hexdigest()
