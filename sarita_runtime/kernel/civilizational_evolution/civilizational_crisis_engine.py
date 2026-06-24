import random

class KnowledgePandemicSimulator:
    def infect(self, institutions):
        # A knowledge pandemic reduces fitness globally
        if random.random() < 0.05:
            for inst in institutions:
                inst["fitness"] *= 0.8
            return True
        return False

class InstitutionalCollapseEngine:
    def check_collapse(self, institution):
        # Sudden collapse if resources are negative or fitness extremely low
        if institution["resources"] < 0 or institution["fitness"] < 0.05:
            institution["status"] = "COLLAPSED"
            return True
        return False

class ResourceScarcityGenerator:
    def generate_scarcity(self):
        # Returns a multiplier for resource consumption
        return 1.5 if random.random() < 0.1 else 1.0

class LegitimacyCrisisDetector:
    def detect(self, institutions):
        # Crisis if average reputation is very low
        avg_rep = sum(i.get("reputation", 1.0) for i in institutions) / len(institutions) if institutions else 1.0
        return avg_rep < 0.5

class CivilizationRecoveryManager:
    def recover(self, institutions):
        # Inject resources into survivors to recover
        for inst in institutions:
            if inst["status"] != "EXTINCT":
                inst["resources"] += 2.0
                inst["fitness"] = max(inst["fitness"], 0.2)

class CivilizationalCrisisEngine:
    def __init__(self):
        self.pandemic = KnowledgePandemicSimulator()
        self.collapse = InstitutionalCollapseEngine()
        self.scarcity = ResourceScarcityGenerator()
        self.legitimacy = LegitimacyCrisisDetector()
        self.recovery = CivilizationRecoveryManager()

    def process_crisis(self, institutions):
        crisis_active = False

        if self.pandemic.infect(institutions):
            crisis_active = True

        multiplier = self.scarcity.generate_scarcity()
        if multiplier > 1.0:
            crisis_active = True
            for inst in institutions:
                inst["resources"] -= 0.5 * multiplier

        if self.legitimacy.detect(institutions):
            crisis_active = True
            for inst in institutions:
                inst["fitness"] *= 0.9

        # Check for collapses
        for inst in institutions:
            self.collapse.check_collapse(inst)

        return crisis_active

    def trigger_recovery(self, institutions):
        self.recovery.recover(institutions)
