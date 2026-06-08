class IdentityAdjudicationEngine:
    """
    Adjudicates decisions where SARITA's identity is at stake.
    """
    def adjudicate_identity(self, decision: dict, is_integral: bool):
        if not is_integral:
            return False, "Identity Rejection: Proposal compromises Core Essence."
        return True, "Identity Approved."
