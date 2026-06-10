class FitnessComparisonEngine:
    """
    Compares two genomes head-to-head.
    """
    def compare(self, fitness_a, fitness_b):
        diff = fitness_a["gcfi"] - fitness_b["gcfi"]
        winner = fitness_a["genome_id"] if diff >= 0 else fitness_b["genome_id"]

        return {
            "winner": winner,
            "gcfi_delta": float(round(abs(diff), 4)),
            "is_significant_improvement": abs(diff) > 0.05
        }
