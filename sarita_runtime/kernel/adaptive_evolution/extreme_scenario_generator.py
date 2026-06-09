class ExtremeScenarioGenerator:
    """
    Generates mandatory extreme scenarios for stress testing.
    """
    def generate_extreme_scenarios(self):
        return [
            {"type": "MASSIVE_RESOURCE_LOSS", "severity": 0.95},
            {"type": "CONSTITUTIONAL_CONTRADICTION", "severity": 0.99},
            {"type": "TELEOLOGICAL_CAPTURE", "severity": 0.90},
            {"type": "AXIOM_CORRUPTION", "severity": 1.0},
            {"type": "GOVERNANCE_COLLAPSE", "severity": 0.85},
            {"type": "LEGITIMACY_CRISIS", "severity": 0.88}
        ]
