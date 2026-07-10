import hashlib
import random

class CosmosGenomeBuilder:
    """
    Builds the 'genome' of a cosmos, defining its fundamental parameters,
    architectural constraints, and initial causal seeds.
    """
    def __init__(self):
        self.traits = [
            "causality_linearity", "logical_entropy", "dimensionality",
            "temporal_flow", "expansion_rate", "observer_potential",
            "physical_constant_stability", "meta_reality_permeability"
        ]

    def build_genome(self, parent_genome=None, divergence=0.05):
        """
        Generates a new cosmos genome, optionally based on a parent genome.
        """
        if parent_genome:
            return self._mutate_genome(parent_genome, divergence)

        genome = {trait: round(random.uniform(0.1, 1.0), 4) for trait in self.traits}
        genome["signature"] = self._calculate_signature(genome)
        return genome

    def _mutate_genome(self, parent_genome, divergence):
        new_genome = {}
        for trait, value in parent_genome.items():
            if trait == "signature":
                continue
            mutation = random.uniform(-divergence, divergence)
            new_value = max(0.0001, min(1.0, value + mutation))
            new_genome[trait] = round(new_value, 4)

        new_genome["signature"] = self._calculate_signature(new_genome)
        return new_genome

    def _calculate_signature(self, genome):
        raw_data = "".join([f"{k}:{v}" for k, v in sorted(genome.items()) if k != "signature"])
        return hashlib.sha256(raw_data.encode()).hexdigest()
