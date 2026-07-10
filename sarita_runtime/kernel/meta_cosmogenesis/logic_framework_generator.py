import random

class LogicFrameworkGenerator:
    """
    Generates the logical axioms that govern reasoning and existence in a cosmos.
    Can support Classical, Intuitionistic, Fuzzy, or Paraconsistent logic.
    """
    def __init__(self):
        self.logic_types = ["CLASSICAL", "INTUITIONISTIC", "FUZZY", "PARACONSISTENT", "MODAL"]

    def generate_framework(self, entropy_seed):
        idx = int(entropy_seed * len(self.logic_types)) % len(self.logic_types)
        logic_type = self.logic_types[idx]

        return {
            "type": logic_type,
            "law_of_excluded_middle": True if logic_type == "CLASSICAL" else False,
            "contradiction_tolerance": round(random.uniform(0.0, 0.5), 4) if logic_type != "PARACONSISTENT" else 0.9,
            "truth_values": 2 if logic_type == "CLASSICAL" else "CONTINUOUS"
        }
