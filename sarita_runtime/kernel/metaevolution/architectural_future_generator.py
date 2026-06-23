import random

class ArchitecturalFutureGenerator:
    """
    Generates the next generation of architectural states.
    """
    def generate_next_generation(self, current_state):
        mutation = random.uniform(-0.01, 0.02)
        return {
            "gen": current_state["gen"] + 1,
            "complexity": current_state.get("complexity", 1.0) + mutation
        }
