class CivilizationDivergenceEngine:
    def __init__(self):
        pass

    def calculate_divergence(self, civ_a, civ_b):
        genome_a = civ_a["genome"]
        genome_b = civ_b["genome"]

        divergence = 0.0
        traits = set(genome_a.keys()) | set(genome_b.keys())

        for trait in traits:
            val_a = genome_a.get(trait, 0.5)
            val_b = genome_b.get(trait, 0.5)
            divergence += abs(val_a - val_b)

        normalized_divergence = divergence / len(traits) if traits else 0.0
        return round(normalized_divergence, 4)

    def analyze_ecosystem_divergence(self, civilizations):
        if len(civilizations) < 2:
            return 0.0

        total_divergence = 0.0
        count = 0
        for i in range(len(civilizations)):
            for j in range(i + 1, len(civilizations)):
                total_divergence += self.calculate_divergence(civilizations[i], civilizations[j])
                count += 1

        return round(total_divergence / count, 4) if count > 0 else 0.0
