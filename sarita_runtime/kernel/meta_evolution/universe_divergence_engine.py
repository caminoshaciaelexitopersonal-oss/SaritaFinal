class UniverseDivergenceEngine:
    def calculate_divergence(self, univ_a, univ_b):
        laws_a = univ_a["laws"]
        laws_b = univ_b["laws"]

        divergence = 0.0
        keys = set(laws_a.keys()) | set(laws_b.keys())
        for key in keys:
            val_a = laws_a.get(key, 0.5)
            val_b = laws_b.get(key, 0.5)
            divergence += abs(val_a - val_b)

        return round(divergence / len(keys), 4) if keys else 0.0

    def analyze_multiverse(self, universes):
        if len(universes) < 2:
            return 0.0

        total_div = 0.0
        count = 0
        for i in range(len(universes)):
            for j in range(i + 1, len(universes)):
                total_div += self.calculate_divergence(universes[i], universes[j])
                count += 1
        return round(total_div / count, 4) if count > 0 else 0.0
