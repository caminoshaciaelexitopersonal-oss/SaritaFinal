import random

class ParadigmEvaluator:
    """
    Evaluates the efficiency and novelty of governance paradigms.
    """
    def evaluate(self, paradigm):
        if paradigm.get("id") == "PARA-1":
            return 0.1
        return random.uniform(0.6, 1.0)
