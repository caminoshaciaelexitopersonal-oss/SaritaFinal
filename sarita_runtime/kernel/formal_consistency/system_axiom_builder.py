from .axiom_registry import AxiomRegistry

class SystemAxiomBuilder:
    """
    Builds the core set of axioms for the SARITA Kernel.
    """
    def __init__(self):
        self.registry = AxiomRegistry()

    def build_core_axioms(self):
        axioms = {
            "A1": "Every module belongs to exactly one valid architecture.",
            "A2": "Every dependency has a valid resolution.",
            "A3": "No engine can circularly depend on itself.",
            "A4": "Every audit has evidence.",
            "A5": "Every certification has an audit.",
            "A6": "Every index has a verifiable calculation.",
            "A7": "Every calculation has traceability.",
            "A8": "Every change has history.",
            "A9": "No component can be orphaned.",
            "A10": "No module can exist without governance."
        }
        for aid, defn in axioms.items():
            self.registry.register_axiom(aid, defn)
        return self.registry
