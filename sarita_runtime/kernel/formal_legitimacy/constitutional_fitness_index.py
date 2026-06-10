class ConstitutionalFitnessIndex:
    """
    Quantifies the system's fitness for survival and evolutionary alignment.
    """

    def calculate_cfi(self,
                      evolutionary_efficiency: float,
                      resource_utility: float,
                      risk_mitigation: float) -> float:
        """
        CFI measures how well the constitution adapts while maintaining core values.
        """
        # Simple weighted average for the index
        cfi = (evolutionary_efficiency * 0.3) + (resource_utility * 0.4) + (risk_mitigation * 0.3)
        return float(round(max(0.0, min(1.0, cfi)), 4))
