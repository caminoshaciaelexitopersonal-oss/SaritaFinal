class ConstitutionalOverrideAnalyzer:
    """Analyzes constitutional overrides and exceptions."""
    def analyze_overrides(self, state):
        return state.get("overrides", [])
