import random

class KnowledgeWarfareSimulator:
    def __init__(self):
        pass

    def execute_intellectual_strike(self, attacker, target):
        attacker_epistemic = attacker["genome"].get("epistemic_openness", 0.5)
        target_rigidity = target["genome"].get("constitutional_rigidity", 0.5)

        strike_success = attacker_epistemic > target_rigidity + random.uniform(-0.2, 0.2)

        if strike_success:
            # Target loses some coherence/resources
            return True, "Epistemic breach successful"
        return False, "Intellectual strike parried"
