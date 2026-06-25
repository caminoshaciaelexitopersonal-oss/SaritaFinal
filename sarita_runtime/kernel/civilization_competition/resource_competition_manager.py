import random

class ResourceCompetitionManager:
    def __init__(self):
        self.global_resources = 1000.0
        self.civ_resources = {}

    def allocate_initial_resources(self, civ_id):
        self.civ_resources[civ_id] = 100.0
        self.global_resources -= 100.0

    def resolve_competition(self, civilizations):
        if not civilizations:
            return

        total_demand = len(civilizations) * 10.0
        available = min(self.global_resources, total_demand)

        # Resources are distributed based on competitive_intensity trait
        demands = []
        for civ in civilizations:
            intensity = civ["genome"].get("governance_centralization", 0.5)
            demands.append(intensity + random.uniform(0, 0.5))

        total_intensity = sum(demands)
        for i, civ in enumerate(civilizations):
            civ_id = civ["identity"]["id"]
            share = (demands[i] / total_intensity) * available
            self.civ_resources[civ_id] = self.civ_resources.get(civ_id, 0) + share
            self.global_resources -= share

        # Passive resource consumption
        for civ_id in self.civ_resources:
            self.civ_resources[civ_id] *= 0.95

    def get_resources(self, civ_id):
        return self.civ_resources.get(civ_id, 0)
