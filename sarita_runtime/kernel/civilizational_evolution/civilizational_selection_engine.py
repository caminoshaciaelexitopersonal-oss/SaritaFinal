import random

class FitnessPressureGenerator:
    def apply_pressure(self, institution, global_difficulty):
        # Global difficulty reduces resources/fitness
        institution["resources"] -= global_difficulty * 0.1
        institution["fitness"] -= global_difficulty * 0.05

class InstitutionalSelectionAnalyzer:
    def analyze_survival_probability(self, institution):
        # Probability of survival based on fitness and resources
        prob = (institution["fitness"] * 0.7) + (min(1.0, institution["resources"] / 10.0) * 0.3)
        return prob

class CompetitiveExtinctionEngine:
    def evaluate_extinction(self, institutions):
        if not institutions:
            return []

        # Bottom 10% in fitness are at high risk
        sorted_inst = sorted(institutions, key=lambda x: x["fitness"])
        num_at_risk = max(1, len(institutions) // 10)
        at_risk = sorted_inst[:num_at_risk]

        survivors = sorted_inst[num_at_risk:]
        for inst in at_risk:
            if random.random() > 0.3: # 70% chance of extinction for bottom tier
                inst["status"] = "EXTINCT"
            else:
                survivors.append(inst)
        return survivors

class AdaptationSurvivalTracker:
    def __init__(self):
        self.history = []

    def record_survival(self, institution_id, fitness):
        self.history.append({"id": institution_id, "fitness": fitness})

class EvolutionaryAdvantageDetector:
    def detect_advantage(self, institution):
        # Advantage if fitness > 0.8
        return institution["fitness"] > 0.8

class CivilizationalSelectionEngine:
    def __init__(self):
        self.pressure = FitnessPressureGenerator()
        self.analyzer = InstitutionalSelectionAnalyzer()
        self.extinction = CompetitiveExtinctionEngine()
        self.tracker = AdaptationSurvivalTracker()
        self.advantage = EvolutionaryAdvantageDetector()

    def select(self, institutions, global_difficulty=0.1):
        for inst in institutions:
            self.pressure.apply_pressure(inst, global_difficulty)
            inst["survival_prob"] = self.analyzer.analyze_survival_probability(inst)
            inst["has_advantage"] = self.advantage.detect_advantage(inst)
            self.tracker.record_survival(inst["id"], inst["fitness"])

        return self.extinction.evaluate_extinction(institutions)

    def get_selection_metrics(self):
        return {
            "avg_survival_prob": sum(h["fitness"] for h in self.tracker.history[-10:]) / 10 if self.tracker.history else 0
        }
