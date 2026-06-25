import random

class InnovationRaceEngine:
    def __init__(self):
        self.innovation_levels = {} # civ_id -> level

    def advance_innovation(self, civ_id, focus):
        current_level = self.innovation_levels.get(civ_id, 0.0)
        # focus is derived from genome 'technological_focus'
        advance = (focus * 0.1) + (random.random() * 0.05)
        self.innovation_levels[civ_id] = round(current_level + advance, 4)
        return self.innovation_levels[civ_id]

    def get_innovation_leader(self):
        if not self.innovation_levels:
            return None
        return max(self.innovation_levels.items(), key=lambda x: x[1])
