import random

class CosmicCompetitionEngine:
    """
    Manages competition between different cosmos for dominance or survival.
    Phase 127.5 - Cosmic Competition Engine.
    """
    def __init__(self):
        self.survival_history = {}

    def track_survival(self, cosmos_list):
        for cosmos in cosmos_list:
            cid = cosmos["identity"]["id"]
            if cid not in self.survival_history:
                self.survival_history[cid] = {"age": 0, "fitness_log": []}
            self.survival_history[cid]["age"] = cosmos["age"]

    def conduct_competition(self, cosmos_a, cosmos_b):
        """
        Simulates a 'collision' or competition between two cosmos.
        """
        fitness_a = self._calculate_fitness(cosmos_a)
        fitness_b = self._calculate_fitness(cosmos_b)

        # Pressure: the stronger cosmos exerts pressure on the weaker
        if fitness_a > fitness_b:
            pressure = (fitness_a - fitness_b) * 0.1
            self._apply_reality_pressure(cosmos_b, pressure)
            return cosmos_a["identity"]["id"]
        else:
            pressure = (fitness_b - fitness_a) * 0.1
            self._apply_reality_pressure(cosmos_a, pressure)
            return cosmos_b["identity"]["id"]

    def _calculate_fitness(self, cosmos):
        # Fitness is a function of genome stability and architecture consistency
        genome_vals = [v for k, v in cosmos["genome"].items() if k != "signature"]
        base_fitness = sum(genome_vals) / len(genome_vals)
        consistency = cosmos.get("architecture", {}).get("consistency_score", 0.5)

        fitness = (base_fitness * 0.4) + (consistency * 0.6)
        return round(fitness, 4)

    def _apply_reality_pressure(self, cosmos, pressure):
        # Pressure reduces consistency or 'destabilizes' the cosmos
        if "architecture" in cosmos:
            cosmos["architecture"]["consistency_score"] = max(0.0, cosmos["architecture"]["consistency_score"] - pressure)

    def rank_cosmos(self, cosmos_list):
        ranked = sorted(cosmos_list, key=lambda x: self._calculate_fitness(x), reverse=True)
        return ranked

    def select_survivors(self, cosmos_list, max_survivors=3):
        ranked = self.rank_cosmos(cosmos_list)
        return ranked[:max_survivors], ranked[max_survivors:]
