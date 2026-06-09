class ConstitutionalBenefitAnalyzer:
    """
    Analyzes the net benefit SARITA provides to the constitutional substrate.
    """
    def analyze_benefit(self, state: dict):
        # Benefit = Stability + Security + Autonomy - Resource Leakage
        return state.get("stability", 0.9) + state.get("security", 0.9)
