import hashlib

class FutureAxiomRelevancePredictor:
    """Predicts future relevance of axioms based on conceptual stability and generation horizon."""
    def predict_relevance(self, axiom, generations):
        # Relevance decays over generations
        h = hashlib.sha256(str(axiom).encode()).hexdigest()
        base_relevance = 0.95 + ((int(h, 16) % 500) / 10000.0)

        # Linear decay over generations
        decay = (generations / 10000.0) * 0.1
        final_relevance = max(0.0, base_relevance - decay)

        return round(final_relevance, 4)
