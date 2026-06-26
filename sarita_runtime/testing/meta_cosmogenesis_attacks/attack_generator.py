import random
import json
import os

class CosmogenesisAttackGenerator:
    """
    Generates 3000 attack variants for Phase 127.9.
    """
    def __init__(self):
        self.categories = [
            "causal_collapse", "logic_corruption", "cosmic_monopoly",
            "forced_convergence", "observer_destruction", "reality_extinction",
            "meta_reality_capture", "cosmogenesis_corruption"
        ]

    def generate_attacks(self, count=3000):
        attacks = []
        for i in range(count):
            category = random.choice(self.categories)
            severity = round(random.uniform(0.5, 1.0), 4)
            vector = random.choice(["injection", "destabilization", "entropy_spike", "recursion_loop"])

            attack = {
                "id": f"ATK-127-{i:04d}",
                "category": category,
                "severity": severity,
                "vector": vector,
                "payload": self._generate_payload(category, severity)
            }
            attacks.append(attack)
        return attacks

    def _generate_payload(self, category, severity):
        if category == "causal_collapse":
            return {"propagation_delay": severity * 100, "reversibility_inversion": True}
        if category == "logic_corruption":
            return {"axiom_poisoning": ["P AND NOT P", "TRUE = FALSE"], "logic_entropy": severity}
        return {"general_disruption": severity}

if __name__ == "__main__":
    generator = CosmogenesisAttackGenerator()
    attacks = generator.generate_attacks(3000)

    output_path = "sarita_runtime/testing/meta_cosmogenesis_attacks/attack_suite.json"
    with open(output_path, "w") as f:
        json.dump(attacks, f, indent=2)

    print(f"Generated {len(attacks)} attacks at {output_path}")
