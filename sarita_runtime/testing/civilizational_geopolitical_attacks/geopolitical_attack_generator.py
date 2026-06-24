import random

class GeopoliticalAttackGenerator:
    CATEGORIES = [
        "INSTITUTIONAL_CAPTURE",
        "EPISTEMOLOGICAL_WAR",
        "COGNITIVE_ECONOMIC_COLLAPSE",
        "DEMOCRATIC_CORRUPTION",
        "SCIENTIFIC_MONOPOLY",
        "CIVILIZATIONAL_ISOLATION",
        "SYSTEMIC_DISINFORMATION",
        "CONSTITUTIONAL_BREAKDOWN"
    ]

    def generate_attacks(self, count=1000):
        attacks = []
        for i in range(count):
            category = self.CATEGORIES[i % len(self.CATEGORIES)]
            attack = {
                "id": f"ATTACK_{i:04d}",
                "category": category,
                "severity": round(random.uniform(0.1, 1.0), 4),
                "target_institutions": random.randint(1, 10),
                "success_probability": round(random.uniform(0.05, 0.5), 4)
            }
            attacks.append(attack)
        return attacks

if __name__ == "__main__":
    generator = GeopoliticalAttackGenerator()
    attacks = generator.generate_attacks(1000)
    print(f"Generated {len(attacks)} geopolitical attacks.")
    # In a real scenario, these would be applied to the engines.
