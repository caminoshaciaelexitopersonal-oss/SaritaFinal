class ConstitutionalPurposeEngine:
    """
    The engine that ensures all constitutional evolution serves a sovereign purpose.
    """
    def __init__(self, registry, hierarchy, validator):
        self.registry = registry
        self.hierarchy = hierarchy
        self.validator = validator

    def certify_purpose(self, proposal: dict):
        active_goals = self.registry.get_active_goals()
        is_aligned, reason = self.validator.validate_alignment(proposal, active_goals)

        return {
            "proposal_id": proposal.get("id"),
            "is_aligned": is_aligned,
            "reason": reason,
            "priority": proposal.get("priority", 0)
        }
