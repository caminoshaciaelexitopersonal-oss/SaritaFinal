import uuid
import copy
from .constitutional_genome import ConstitutionalGenome

class ConstitutionalMutationEngine:
    """
    Applies controlled mutations to constitutional genes.
    """
    def mutate(self, genome):
        mutated_genome = copy.deepcopy(genome)
        mutated_genome.genome_id = f"VAR-{uuid.uuid4()}"
        mutated_genome.parent_id = genome.genome_id

        # In Phase 103, we simulate a mutation by subtly altering a gene's expression
        gene_to_mutate = list(mutated_genome.genes.keys())[0] if mutated_genome.genes else "RULE"
        original_expr = mutated_genome.genes.get(gene_to_mutate, "DEFAULT")
        mutated_genome.genes[gene_to_mutate] = f"MODIFIED({original_expr})"

        return mutated_genome
