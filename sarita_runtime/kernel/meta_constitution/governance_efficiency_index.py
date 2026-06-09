class GovernanceEfficiencyIndex:
    """
    Calculates the efficiency of governance.
    Efficiency = System Stability / Constitutional Complexity
    """
    def calculate(self, stability: float, complexity: float):
        if complexity <= 0:
            return 1.0
        return stability / complexity
