class EvolutionConstraintEngine:
    """
    Engine that enforces civilizational constraints on SARITA's evolution.
    """
    def __init__(self, boundary_mgr, deviation_detector, limit_validator):
        self.boundary_mgr = boundary_mgr
        self.deviation_detector = deviation_detector
        self.limit_validator = limit_validator

    def enforce_constraints(self, proposed_evolution: dict):
        boundary_ok = self.boundary_mgr.check_boundary(proposed_evolution.get("type"))
        deviation = self.deviation_detector.detect_deviation("FASE_1", proposed_evolution.get("purpose"))
        limit_ok = self.limit_validator.validate_evolution_limit(proposed_evolution.get("cycles", 0))

        is_constrained = boundary_ok and (deviation < 0.15) and limit_ok

        return {
            "is_within_limits": is_constrained,
            "deviation_score": deviation,
            "boundary_check": "PASSED" if boundary_ok else "FAILED",
            "verdict": "ALLOWED" if is_constrained else "BLOCKED"
        }
