import uuid
from .constitutional_genome import ConstitutionalGenome

class ConstitutionalCrossoverEngine:
    """
    Combines genes from two parent genomes into a new hybrid constitution.
    """
    def crossover(self, parent_a, parent_b):
        child_id = f"HYB-{uuid.uuid4()}"
        child = ConstitutionalGenome(child_id, parent_id=f"{parent_a.genome_id}+{parent_b.genome_id}")

        # Interleave genes from parents
        all_gene_types = set(parent_a.genes.keys()).union(set(parent_b.genes.keys()))
        for i, gene_type in enumerate(all_gene_types):
            if i % 2 == 0:
                child.add_gene(gene_type, parent_a.genes.get(gene_type))
            else:
                child.add_gene(gene_type, parent_b.genes.get(gene_type))

        return child
