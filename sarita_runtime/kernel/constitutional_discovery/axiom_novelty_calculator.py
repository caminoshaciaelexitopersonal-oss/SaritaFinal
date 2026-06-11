import random

class AxiomNoveltyCalculator:
    """
    Calculates the novelty of a new axiom.
    """
    def calculate(self, axiom):
        # Compares with "Identity", "Purpose", "Legitimacy"
        # High score means it is conceptually distant from foundations.
        statement = axiom.get("statement", "")

        # Check for direct plagiarism
        if statement == "KNOWN":
            return 0.1

        # Conceptual distance based on primitives
        foundational_primitives = {"Identity", "Purpose", "Legitimacy", "Sovereignty"}
        axiom_primitives = set(axiom.get("primitives", []))

        overlap = len(axiom_primitives.intersection(foundational_primitives))
        distance = 1.0 - (overlap / max(1, len(axiom_primitives)))

        return max(0.1, distance)
