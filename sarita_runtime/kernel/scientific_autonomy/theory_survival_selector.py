class TheorySurvivalSelector:
    def select_survivors(self, theory_scores, survival_threshold=0.7):
        # Selects theories that survive based on empirical fitness
        return [t_id for t_id, score in theory_scores.items() if score >= survival_threshold]
