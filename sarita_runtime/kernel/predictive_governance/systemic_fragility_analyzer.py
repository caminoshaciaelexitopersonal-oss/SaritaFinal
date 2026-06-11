class SystemicFragilityAnalyzer:
    """
    Analyzes the structural fragility of the governance system.
    """
    def analyze_fragility(self, structural_data):
        """
        Measures structural susceptibility to perturbations.
        """
        if not structural_data:
            return 0.0
        fragility_score = sum(structural_data.values()) / len(structural_data)
        return fragility_score
