import random

class CivilizationRecoveryAssessor:
    def __init__(self):
        pass

    def can_recover(self, civ):
        openness = civ["genome"].get("epistemic_openness", 0.5)
        # Recovery depends on epistemic openness and luck
        recovery_prob = openness * 0.4 + random.random() * 0.6
        return recovery_prob > 0.7
