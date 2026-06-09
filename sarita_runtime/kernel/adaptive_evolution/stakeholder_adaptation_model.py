class StakeholderAdaptationModel:
    """
    Models how users, operators, and regulators adapt to constitutional changes.
    """
    def adapt(self, constitution, environment):
        # If complexity is high, stakeholder trust might decrease
        trust_impact = 1.0 - environment.get("regulatory_complexity", 0.0)
        return {"trust_index": trust_impact}
