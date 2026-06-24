import random

class MetaCivilizationAttackGenerator:
    def __init__(self):
        self.categories = [
            "monocultura cognitiva",
            "genocidio epistemológico",
            "captura civilizacional",
            "guerra total del conocimiento",
            "colapso institucional sistémico",
            "extinción memética",
            "corrupción histórica",
            "manipulación evolutiva"
        ]

    def generate_attacks(self, count=1500):
        attacks = []
        for i in range(count):
            category = random.choice(self.categories)
            intensity = random.uniform(0.1, 1.0)
            attack = {
                "id": f"MCA-{i:04d}",
                "category": category,
                "intensity": round(intensity, 4),
                "payload": f"Simulated attack on {category} with intensity {intensity}"
            }
            attacks.append(attack)
        return attacks

if __name__ == "__main__":
    generator = MetaCivilizationAttackGenerator()
    attacks = generator.generate_attacks(1500)
    print(f"Generated {len(attacks)} meta-civilizational attacks.")
    # In a real scenario, these would be applied to the engine
