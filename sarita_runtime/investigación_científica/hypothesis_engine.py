class ScientificHypothesis:
    """
    Formally encapsulates a scientific hypothesis with independent, dependent, nula, and alternative variables,
    along with risks, control variables, and limitations.
    """
    def __init__(self, hypothesis_id: str, objective: str, independent_var: str, dependent_var: str,
                 null_hypothesis: str, alternative_hypothesis: str, control_vars: list = None,
                 risks: list = None, limitations: list = None):
        self.hypothesis_id = hypothesis_id
        self.objective = objective
        self.independent_var = independent_var
        self.dependent_var = dependent_var
        self.null_hypothesis = null_hypothesis
        self.alternative_hypothesis = alternative_hypothesis
        self.control_vars = control_vars or []
        self.risks = risks or []
        self.limitations = limitations or []
        self.status = "FORMULATED"  # FORMULATED, TESTING, ACCEPTED, REJECTED, REVISED

    def to_dict(self) -> dict:
        return {
            "hypothesis_id": self.hypothesis_id,
            "objective": self.objective,
            "independent_var": self.independent_var,
            "dependent_var": self.dependent_var,
            "null_hypothesis": self.null_hypothesis,
            "alternative_hypothesis": self.alternative_hypothesis,
            "control_vars": self.control_vars,
            "risks": self.risks,
            "limitations": self.limitations,
            "status": self.status
        }
