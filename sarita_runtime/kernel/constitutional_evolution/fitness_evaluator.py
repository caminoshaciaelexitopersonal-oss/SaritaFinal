class FitnessEvaluator:
    """
    Calculates specific fitness sub-metrics for a given genome based on its structure.
    """
    def calculate_sub_fitness(self, genome):
        """
        Derives fitness by analyzing gene complexity and completeness.
        """
        return {
            "legitimacy_fitness": self._evaluate_gene(genome, "AXIOM"),
            "identity_fitness": self._evaluate_gene(genome, "INVARIANT"),
            "purpose_fitness": self._evaluate_gene(genome, "RULE"),
            "governance_fitness": self._evaluate_gene(genome, "CONSTRAINT"),
            "optimality_fitness": self._evaluate_gene(genome, "METRIC"),
            "survival_fitness": self._evaluate_gene(genome, "EVOLUTION_LIMIT"),
            "civilizational_fitness": 1.0 # Constant foundational fidelity
        }

    def _evaluate_gene(self, genome, gene_type):
        gene = genome.get_gene(gene_type)
        if not gene:
            return 0.0

        # Calculate fitness based on gene content length as a proxy for complexity/specificity
        content_score = len(str(gene)) / 100.0
        return float(round(min(1.0, 0.8 + content_score), 4))
