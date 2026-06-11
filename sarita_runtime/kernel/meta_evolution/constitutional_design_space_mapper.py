import random

class ConstitutionalDesignSpaceMapper:
    """
    Maps the high-dimensional space of civilizational possibilities.
    """

    DIMENSIONS = [
        "centralization", # 0.0 (Distributed) -> 1.0 (Unitary)
        "volatility",      # 0.0 (Static) -> 1.0 (Hyper-evolving)
        "rigidity",        # 0.0 (Fluid) -> 1.0 (Absolute)
        "complexity",      # 0.0 (Simple) -> 1.0 (Advanced)
        "altruism",        # 0.0 (Selfish) -> 1.0 (Cooperative)
        "foresight"        # 0.0 (Short-term) -> 1.0 (Millennial)
    ]

    def sample_design_space(self):
        """
        Returns a random sample from the design space.
        """
        return {dim: random.uniform(0.0, 1.0) for dim in self.DIMENSIONS}

    def calculate_distance(self, meta_a, meta_b):
        """
        Calculates the topological distance between two meta-constitutions.
        """
        # Uses the Euclidean distance between shared design dimensions.
        dist = 0
        for dim in self.DIMENSIONS:
            val_a = meta_a.governance_structure.get(dim, 0.5)
            val_b = meta_b.governance_structure.get(dim, 0.5)
            dist += (val_a - val_b) ** 2
        return dist ** 0.5
