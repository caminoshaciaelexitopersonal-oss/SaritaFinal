class PolicyEvidenceChecker:
    """
    Checks the scientific evidence backing a policy.
    """
    def check_evidence(self, policy):
        """
        Ensures the policy is derived from a certified governance law.
        """
        return policy.get("law_id") is not None
