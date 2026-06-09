import time

class FoundationalPrincipleRegistry:
    """
    Registry for SARITA's foundational civilizational principles.
    """
    def __init__(self):
        self.principles = {
            "HUMAN_CENTERED_SOVEREIGNTY": {"origin": "Fase 1", "immutable": True},
            "ETHICAL_DETERMINISM": {"origin": "Fase 1", "immutable": True},
            "CAUSAL_FIDELITY": {"origin": "Fase 1", "immutable": True}
        }

    def get_foundational_set(self):
        return set(self.principles.keys())
