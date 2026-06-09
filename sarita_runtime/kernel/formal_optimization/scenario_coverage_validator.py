class ScenarioCoverageValidator:
    """
    Validates if a specific scenario has sufficient axiomatic backing.
    """
    def validate_coverage(self, scenario, axioms):
        relevant_axioms = [a for a in axioms if self._is_backed(scenario, a)]
        return len(relevant_axioms) > 0

    def _is_backed(self, scenario, axiom):
        return any(tag.upper() in str(axiom).upper() for tag in scenario.get("tags", []))
