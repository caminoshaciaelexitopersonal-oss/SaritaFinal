class ConstitutionalStructureMapper:
    """
    Maps genome sequences back to the active constitutional structure.
    """
    def map_to_kernel(self, genome):
        # In Phase 103, this provides the mapping instructions for the kernel
        # to apply the genome's genes into the active engines.
        mapping = {}
        for gene_type, expression in genome.genes.items():
            mapping[gene_type] = {
                "target_engine": self._resolve_target(gene_type),
                "expression": expression
            }
        return mapping

    def _resolve_target(self, gene_type):
        targets = {
            "AXIOM": "ConstitutionalAxiomRegistry",
            "CONSTRAINT": "FormalProofEngine",
            "INVARIANT": "ConstitutionalInvariantEngine",
            "METRIC": "ConstitutionalMetricEngine",
            "RULE": "DeductiveReasoner",
            "EVOLUTION_LIMIT": "ConstitutionalReformEngine"
        }
        return targets.get(gene_type, "Unknown")
