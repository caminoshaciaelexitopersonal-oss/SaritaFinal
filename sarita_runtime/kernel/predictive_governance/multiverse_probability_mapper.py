class MultiverseProbabilityMapper:
    """
    Maps probabilities across thousands of multiversal scenarios.
    """
    def map_probabilities(self, scenarios):
        """
        Assigns probability weights based on scenario stability and legitimacy.
        """
        # Calculate scores for each scenario
        scores = {}
        for name, params in scenarios.items():
            # In a real engine, this is derived from the frequency of the scenario in 10,000 universes
            # Here we use the product of stability indicators as a proxy for likelihood
            scores[name] = params.get("legitimacy", 0.5) * params.get("stability", 0.5)

        total_score = sum(scores.values())
        if total_score == 0:
            return {name: 1.0 / len(scenarios) for name in scenarios}

        return {name: score / total_score for name, score in scores.items()}
