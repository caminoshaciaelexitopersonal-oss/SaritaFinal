class ConstitutionalSelectionEngine:
    """
    Selects the best performing constitutional variants.
    """
    def select_next_generation(self, scored_variants, top_k=10):
        # Sort by GCFI descending
        sorted_variants = sorted(scored_variants, key=lambda x: x[1]["gcfi"], reverse=True)
        # Return only the genomes of the top k
        return [v[0] for v in sorted_variants[:top_k]]
