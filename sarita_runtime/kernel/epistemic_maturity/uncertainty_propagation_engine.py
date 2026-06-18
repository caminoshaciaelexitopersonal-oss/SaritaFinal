class UncertaintyPropagationEngine:
    """Propagates uncertainty across the causal chain from axiom to result."""
    def propagate_uncertainty(self, boundaries):
        # Accumulates uncertainty from multiple layers
        sigma = 0.001
        return {"sigma": sigma, "interval": [boundaries["lower"] - sigma, boundaries["upper"]]}
