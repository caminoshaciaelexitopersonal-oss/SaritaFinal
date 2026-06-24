import random
from .knowledge_currency_system import KnowledgeCurrencySystem
from .attention_economy_manager import AttentionEconomyManager
from .research_capital_allocator import ResearchCapitalAllocator
from .reputation_market_engine import ReputationMarketEngine
from .scientific_trade_simulator import ScientificTradeSimulator

class CognitiveMarketEngine:
    def __init__(self):
        self.currency = KnowledgeCurrencySystem()
        self.attention = AttentionEconomyManager()
        self.capital = ResearchCapitalAllocator()
        self.reputation = ReputationMarketEngine()
        self.trade = ScientificTradeSimulator()

    def process_market_cycle(self, institutions):
        attention_map = self.attention.distribute_attention(institutions)
        for inst in institutions:
            perf = (attention_map.get(inst["id"], 0) * inst["fitness"]) - 0.05
            self.reputation.update_reputation(inst, perf)
            self.currency.issue(inst["id"], inst.get("reputation", 1.0) * 0.1)
            self.capital.allocate(inst, self.currency.balance(inst["id"]) * 0.5)

        if len(institutions) >= 2:
            a, b = random.sample(institutions, 2)
            self.trade.simulate_trade(a, b)

    def get_market_metrics(self, institutions):
        if not institutions:
            return {"total_knowledge_currency": 0, "total_research_capital": 0, "reputation_spread": 0}
        reputations = [i.get("reputation", 1.0) for i in institutions]
        return {
            "total_knowledge_currency": sum(self.currency.balance(i["id"]) for i in institutions),
            "total_research_capital": sum(i.get("research_capital", 0) for i in institutions),
            "reputation_spread": max(reputations) - min(reputations)
        }
