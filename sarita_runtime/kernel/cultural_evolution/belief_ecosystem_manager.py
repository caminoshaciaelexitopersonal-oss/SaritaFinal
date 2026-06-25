class BeliefEcosystemManager:
    def __init__(self):
        self.beliefs = {} # civ_id -> list of beliefs

    def add_belief(self, civ_id, belief):
        if civ_id not in self.beliefs:
            self.beliefs[civ_id] = []
        self.beliefs[civ_id].append(belief)

    def evolve_beliefs(self, civ_id, pressure):
        if civ_id not in self.beliefs:
            return

        # Simplified belief evolution: beliefs with low resilience are removed
        self.beliefs[civ_id] = [b for b in self.beliefs[civ_id] if b.get("resilience", 0.5) > (pressure * 0.5)]

    def get_beliefs(self, civ_id):
        return self.beliefs.get(civ_id, [])
