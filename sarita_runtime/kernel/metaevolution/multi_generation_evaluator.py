class MultiGenerationEvaluator:
    """
    Evaluates a specific generation in an evolutionary line.
    """
    def evaluate_generation(self, gen_state):
        # Evaluation based on complexity and generation number
        fitness = 1.0 / (1.0 + abs(gen_state["complexity"] - 1.5))
        return {
            "generation": gen_state["gen"],
            "fitness": fitness
        }
