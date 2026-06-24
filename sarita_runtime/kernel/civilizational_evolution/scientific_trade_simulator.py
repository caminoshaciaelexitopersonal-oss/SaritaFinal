class ScientificTradeSimulator:
    def simulate_trade(self, inst_a, inst_b):
        if inst_a.get("research_capital", 0) > 1.0:
            inst_a["research_capital"] -= 1.0
            inst_b["resources"] += 0.5
            return True
        return False
