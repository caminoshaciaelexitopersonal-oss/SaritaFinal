class ConstitutionalGenome:
    """
    Represents a full constitution as a structured genome of functional genes.
    """
    def __init__(self, genome_id, parent_id=None, mutation_history=None):
        self.genome_id = genome_id
        self.parent_id = parent_id
        self.mutation_history = mutation_history if mutation_history is not None else []
        self.genes = {} # gene_type -> expression

    def add_gene(self, gene_type, expression):
        self.genes[gene_type] = expression

    def get_gene(self, gene_type):
        return self.genes.get(gene_type)

    def record_mutation(self, mutation_details):
        self.mutation_history.append(mutation_details)

    def to_dict(self):
        return {
            "genome_id": self.genome_id,
            "parent_id": self.parent_id,
            "mutation_history": self.mutation_history,
            "genes": {k: str(v) for k, v in self.genes.items()}
        }
