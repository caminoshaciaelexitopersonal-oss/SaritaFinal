class SurvivalAdjudicationEngine:
    """
    Adjudicates decisions where survival is at stake.
    """
    def adjudicate_survival(self, decision: dict):
        # Survival always wins.
        if decision.get("type") == "SURVIVAL":
            return True, "Approved: Survival priority."
        if decision.get("p_s_impact", 0) < 0:
            return False, "Rejected: Negative survival impact."
        return True, "Approved: Neutral/Positive survival impact."
