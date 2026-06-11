import random

class AxiomGenerator:
    """
    Generates new axioms from logical primitives.
    """
    PRIMITIVES = [
        "Sovereignty", "Identity", "Accountability", "Transparency",
        "Efficiency", "Resilience", "Adaptability", "Justice",
        "Collective", "Distributed", "Autonomous", "Recursive"
    ]

    OPERATORS = ["is", "must", "evolves", "constrains", "verifies"]

    def generate_axiom(self):
        # Synthesis of a new logical statement
        subj = random.choice(self.PRIMITIVES)
        op = random.choice(self.OPERATORS)
        obj = random.choice(self.PRIMITIVES)

        return {
            "statement": f"{subj} {op} {obj}",
            "primitives": [subj, obj],
            "operator": op,
            "consistency_score": random.uniform(0.8, 1.0),
            "fitness_score": random.uniform(0.7, 1.0)
        }
