class KnowledgeGrowthEstimator:
    def estimate_growth(self, investment_history):
        # Estimates future growth based on past investment ROI
        return sum(investment_history) / len(investment_history) if investment_history else 0.05
