class CivilizationalOutcomeEvaluator:
    """
    Evaluates and records the state of a civilization.
    """
    def evaluate(self, civilization, generation):
        # Capture current metrics
        metrics = civilization.current_state.copy()
        metrics["generation"] = generation

        # Calculate derived capacity
        metrics["evolutionary_capacity"] = (
            metrics["complexity"] *
            civilization.meta_constitution.evolution_rules.get("mutation_rate", 0.1)
        )

        return metrics
