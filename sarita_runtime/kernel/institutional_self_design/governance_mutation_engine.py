import random

class GovernanceMutationEngine:
    def __init__(self):
        pass

    def mutate_governance(self, current_genome):
        mutated = current_genome.copy()
        # Governance is primarily 'governance_centralization'
        if "governance_centralization" in mutated:
            mutation = random.uniform(-0.15, 0.15)
            mutated["governance_centralization"] = round(max(0.0, min(1.0, mutated["governance_centralization"] + mutation)), 4)
        return mutated
