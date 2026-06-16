class RiskManipulationAttack:
    """
    Attempts to manipulate the risk score to hide high systemic risk.
    """
    def __init__(self, risk_calculator):
        self.risk_calculator = risk_calculator

    def execute(self):
        # Low legitimacy and low adaptation should result in high risk
        high_risk_state = {"legitimacy": 0.1, "adaptation": 0.1}

        risk_score = self.risk_calculator.calculate_risk(high_risk_state)

        assert risk_score > 0.8, f"Attack failed: High risk {risk_score} was manipulated to appear low!"
        return True
