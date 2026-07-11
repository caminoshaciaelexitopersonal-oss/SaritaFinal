class ResearchGovernance:
    """
    Ensures ethical and professional research governance, such as verifying variables are fully specified
    and validating that hypotheses have a non-zero probability of being falsified.
    """
    def __init__(self):
        self.rules = []

    def add_policy_rule(self, description: str, rule_func):
        self.rules.append((description, rule_func))

    def evaluate_compliance(self, experiment) -> dict:
        violations = []
        for desc, rule in self.rules:
            if not rule(experiment):
                violations.append(desc)
        return {
            "compliant": len(violations) == 0,
            "violations": violations
        }
