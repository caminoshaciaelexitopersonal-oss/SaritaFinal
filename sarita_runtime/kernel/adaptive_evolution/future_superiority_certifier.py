class FutureSuperiorityCertifier:
    """
    Certifies the superiority of a constitution based on future competition simulations.
    """
    def calculate_superiority(self, competition_data):
        """
        Superiority = (Winner Final Fitness) / (Average Final Fitness of competitors)
        """
        if not competition_data:
            return 0.0

        winner_fitness = competition_data[0].get("final_fitness", 0.0)

        avg_fitness = sum(c.get("final_fitness", 0.0) for c in competition_data) / len(competition_data)

        if avg_fitness == 0:
            return 1.0

        superiority = winner_fitness / avg_fitness
        return float(round(min(1.0, superiority), 4))
