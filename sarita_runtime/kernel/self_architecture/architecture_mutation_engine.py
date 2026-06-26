import random

class ArchitectureMutationEngine:
    def mutate(self, architecture, rate=0.05):
        genome = architecture["genome"]
        mutated = False
        for trait in genome:
            if trait == "signature": continue
            if random.random() < rate:
                mutation = random.uniform(-0.1, 0.1)
                genome[trait] = round(max(0.0001, min(1.0, genome[trait] + mutation)), 4)
                mutated = True

        if mutated:
            from .architecture_genome_builder import ArchitectureGenomeBuilder
            genome["signature"] = ArchitectureGenomeBuilder()._calculate_signature(genome)
        return mutated

class ArchitectureRecombinationEngine:
    def recombine(self, arch_a, arch_b):
        genome_a = arch_a["genome"]
        genome_b = arch_b["genome"]

        child_genome = {}
        for trait in genome_a:
            if trait == "signature": continue
            child_genome[trait] = (genome_a[trait] + genome_b[trait]) / 2

        from .architecture_genome_builder import ArchitectureGenomeBuilder
        child_genome["signature"] = ArchitectureGenomeBuilder()._calculate_signature(child_genome)
        return child_genome

class ArchitectureExtinctionEngine:
    def evaluate_survival(self, architecture, fitness):
        if fitness < 0.2:
            architecture["status"] = "EXTINCT"
            return True
        return False
