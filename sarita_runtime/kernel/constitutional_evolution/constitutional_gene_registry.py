class ConstitutionalGeneRegistry:
    """
    Registry of all available gene types for constitutional evolution.
    """
    def __init__(self):
        self.gene_definitions = {
            "AXIOM": "Foundational logical truth",
            "CONSTRAINT": "Boundary condition for execution",
            "INVARIANT": "Non-negotiable system state",
            "METRIC": "Quantitative performance measurement",
            "RULE": "Decision-making logic",
            "EVOLUTION_LIMIT": "Constraints on future mutations"
        }

    def get_definitions(self):
        return self.gene_definitions
