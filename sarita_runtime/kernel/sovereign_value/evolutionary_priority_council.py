class EvolutionaryPriorityCouncil:
    """
    Higher-order council that resolves conflicts based on Value and Survival.
    """
    def __init__(self, arbitrator, tradeoff_engine, validator):
        self.arbitrator = arbitrator
        self.tradeoff_engine = tradeoff_engine
        self.validator = validator

    def resolve_priority(self, goal_a: dict, goal_b: dict):
        # 1. Arbitrate
        winner = self.arbitrator.arbitrate(goal_a, goal_b)

        # 2. Check Tradeoff
        gain = winner["value"]
        cost = min(goal_a["value"], goal_b["value"]) # Cost is the lost value of the other goal
        is_worth_it = self.tradeoff_engine.calculate_tradeoff(gain, cost)

        # 3. Validate Survival
        p_ok, msg = self.validator.validate_priority(winner["id"], 10, winner.get("type", "GOAL"))

        return {
            "winner_id": winner["id"],
            "justification": "Survival/Value Superiority",
            "tradeoff_valid": is_worth_it,
            "survival_check": p_ok
        }
