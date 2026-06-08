class OntologicalContinuityEngine:
    """
    Determines if a post-reform evolution is still SARITA.
    """
    def __init__(self, analyzer, validator, checker):
        self.analyzer = analyzer
        self.validator = validator
        self.checker = checker

    def verify_continuity(self, state_before: dict, state_after: dict):
        score = self.analyzer.analyze_preservation(state_before, state_after)
        is_consistent, reason = self.checker.check_consistency(state_after)
        is_still_sarita = self.validator.validate_transition(score) and is_consistent

        return {
            "is_still_sarita": is_still_sarita,
            "preservation_score": score,
            "consistency_report": reason,
            "ontological_verdict": "SAME_ENTITY" if is_still_sarita else "ENTITY_DRIFT"
        }
