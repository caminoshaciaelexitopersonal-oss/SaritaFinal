class GovernanceExperienceBuilder:
    """
    Builds structured experience from historical decisions and outcomes.
    """
    def build_experience(self, action, outcome):
        """
        Creates an experience entry for successes or failures.
        """
        return {"action": action, "outcome": outcome, "timestamp": "t-10"}
