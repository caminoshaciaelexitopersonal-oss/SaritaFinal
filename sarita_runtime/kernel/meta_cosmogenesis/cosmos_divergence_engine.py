import random

class CosmosDivergenceEngine:
    """
    Measures and promotes divergence between different cosmos to avoid cosmological monopoly.
    """
    def calculate_divergence(self, cosmos_a, cosmos_b):
        genome_a = cosmos_a["genome"]
        genome_b = cosmos_b["genome"]

        diffs = []
        for trait in genome_a:
            if trait in ["signature", "id"]: continue
            diffs.append(abs(genome_a[trait] - genome_b[trait]))

        return sum(diffs) / len(diffs) if diffs else 0.0

    def trigger_divergence_event(self, cosmos, intensity=0.1):
        """
        Forcefully shifts a cosmos genome to increase diversity.
        """
        for trait in cosmos["genome"]:
            if trait == "signature": continue
            cosmos["genome"][trait] = round(max(0.0001, min(1.0, cosmos["genome"][trait] + random.uniform(-intensity, intensity))), 4)

        from .cosmos_genome_builder import CosmosGenomeBuilder
        cosmos["genome"]["signature"] = CosmosGenomeBuilder()._calculate_signature(cosmos["genome"])
        return cosmos
