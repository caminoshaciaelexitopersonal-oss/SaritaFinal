class ParadigmSurvivalSelector:
    def select_survivors(self, competition_results, survival_threshold=0.5):
        # Selects paradigms that exceed the survival fitness threshold
        return [p_id for p_id, fitness in competition_results.items() if fitness >= survival_threshold]
