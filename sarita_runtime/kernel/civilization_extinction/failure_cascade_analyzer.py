class FailureCascadeAnalyzer:
    def __init__(self):
        pass

    def analyze_cascade_potential(self, civ, risk):
        rigidity = civ["genome"].get("constitutional_rigidity", 0.5)
        # High rigidity makes failure more likely to cascade once risk is high
        cascade_prob = risk * (0.5 + rigidity)
        return cascade_prob > 0.5
