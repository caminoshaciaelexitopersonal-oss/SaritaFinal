class ConstitutionalConsistencyEvaluator:
    """Evaluates the internal consistency of the constitutional axiom set."""
    def evaluate_consistency(self, axiom_results):
        if not axiom_results:
            return {"score": 0.0}
        avg_validity = sum([a["validity"] for a in axiom_results]) / len(axiom_results)
        return {"score": round(avg_validity, 4)}
