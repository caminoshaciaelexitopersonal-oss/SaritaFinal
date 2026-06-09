class EvolutionarySurvivalCouncil:
    """
    The ultimate authority for evolutionary selection and survival adjudication.
    """
    def __init__(self, adjudicator, priority_mgr, resolver):
        self.adjudicator = adjudicator
        self.priority_mgr = priority_mgr
        self.resolver = resolver

    def resolve_existential_tension(self, decision: dict, p_e: float):
        # 1. Set priority
        priority = self.priority_mgr.set_existential_priority(p_e)

        # 2. Adjudicate survival
        ok, msg = self.adjudicator.adjudicate_survival(decision)

        # 3. Resolve conflict
        winner = self.resolver.resolve_conflict("Growth", "Survival")

        return {
            "verdict": ok,
            "reason": msg,
            "priority": priority,
            "winner": winner
        }
