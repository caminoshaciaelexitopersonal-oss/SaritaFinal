class ConstitutionalRewriteEngine:
    def __init__(self):
        self.rewrite_history = {}

    def rewrite_constitution(self, civ_id, current_genome):
        # A rewrite is a more significant change than a mutation
        new_genome = current_genome.copy()
        if "constitutional_rigidity" in new_genome:
            # Re-evaluating rigidity
            new_genome["constitutional_rigidity"] = round(new_genome["constitutional_rigidity"] * 0.8, 4)

        if civ_id not in self.rewrite_history:
            self.rewrite_history[civ_id] = 0
        self.rewrite_history[civ_id] += 1

        return new_genome
