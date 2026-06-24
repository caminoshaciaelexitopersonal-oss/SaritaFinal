import random

class AllianceManager:
    def form_alliance(self, inst_a, inst_b):
        if inst_b["id"] not in inst_a["alliances"]:
            inst_a["alliances"].append(inst_b["id"])
        if inst_a["id"] not in inst_b["alliances"]:
            inst_b["alliances"].append(inst_a["id"])

class TreatyNegotiationEngine:
    def negotiate(self, inst_a, inst_b):
        # Increased success probability to ensure evidence generation
        success_prob = 0.6
        if inst_a["type"] == inst_b["type"]:
            success_prob += 0.3
        return random.random() < success_prob

class InstitutionalDiplomacyEngine:
    def evaluate_relations(self, inst_a, inst_b):
        if inst_b["id"] in inst_a["alliances"]:
            return "FRIENDLY"
        if inst_a["type"] != inst_b["type"] and random.random() < 0.1:
            return "HOSTILE"
        return "NEUTRAL"

class ConflictResolutionEngine:
    def resolve(self, inst_a, inst_b):
        if inst_a["fitness"] > inst_b["fitness"]:
            inst_b["resources"] -= 0.1
            return inst_a["id"]
        else:
            inst_a["resources"] -= 0.1
            return inst_b["id"]

class SovereigntyValidator:
    def validate(self, institution):
        return institution["resources"] > 0.05 and institution["fitness"] > 0.05

class CognitiveGeopoliticsEngine:
    def __init__(self):
        self.alliances = AllianceManager()
        self.treaties = TreatyNegotiationEngine()
        self.diplomacy = InstitutionalDiplomacyEngine()
        self.conflicts = ConflictResolutionEngine()
        self.sovereignty = SovereigntyValidator()
        self.active_treaties = []

    def update_geopolitics(self, institutions):
        if len(institutions) < 2:
            return

        for _ in range(len(institutions)):
            a, b = random.sample(institutions, 2)
            if a["id"] == b["id"]: continue

            rel = self.diplomacy.evaluate_relations(a, b)

            if rel == "NEUTRAL":
                if self.treaties.negotiate(a, b):
                    self.alliances.form_alliance(a, b)
                    self.active_treaties.append((a["id"], b["id"]))

            if rel == "HOSTILE":
                self.conflicts.resolve(a, b)

        for inst in institutions:
            inst["sovereign"] = self.sovereignty.validate(inst)

    def get_geopolitical_metrics(self):
        return {
            "active_treaties_count": len(self.active_treaties)
        }
