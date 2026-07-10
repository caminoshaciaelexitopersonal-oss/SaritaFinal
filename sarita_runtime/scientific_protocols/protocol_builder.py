class Protocol:
    """
    Represents a formal scientific operating protocol definition.
    """
    def __init__(self, name: str, version: str = "1.0.0"):
        self.name = name
        self.version = version
        self.hypothesis = ""
        self.control_variables = {}
        self.independent_variables = {}
        self.dependent_variables = {}
        self.experimental_design = ""
        self.procedure = []
        self.repetitions = 10
        self.initial_conditions = {}
        self.acceptance_criteria = []
        self.rejection_criteria = []
        self.limitations = []

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "version": self.version,
            "hypothesis": self.hypothesis,
            "variables": {
                "control": self.control_variables,
                "independent": self.independent_variables,
                "dependent": self.dependent_variables
            },
            "experimental_design": self.experimental_design,
            "procedure": self.procedure,
            "repetitions": self.repetitions,
            "initial_conditions": self.initial_conditions,
            "acceptance_criteria": self.acceptance_criteria,
            "rejection_criteria": self.rejection_criteria,
            "limitations": self.limitations
        }

class ProtocolBuilder:
    """
    Builder pattern to synthesize formal scientific protocols with complete parameters.
    """
    def __init__(self, name: str):
        self.protocol = Protocol(name)

    def set_hypothesis(self, hyp: str):
        self.protocol.hypothesis = hyp
        return self

    def add_variable(self, category: str, name: str, default_val):
        if category == "control":
            self.protocol.control_variables[name] = default_val
        elif category == "independent":
            self.protocol.independent_variables[name] = default_val
        elif category == "dependent":
            self.protocol.dependent_variables[name] = default_val
        return self

    def set_repetitions(self, reps: int):
        self.protocol.repetitions = reps
        return self

    def build(self) -> Protocol:
        return self.protocol
