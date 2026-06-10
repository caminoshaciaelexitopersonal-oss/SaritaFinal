class HistoricalEffectivenessEngine:
    """
    Quantifies the effectiveness of reforms over long time horizons.
    """
    def calculate_effectiveness(self, reform_history):
        # Effectiveness = sum(improvements) / total_reforms
        improvements = [r for r in reform_history if r["outcome"] == "IMPROVED"]
        return len(improvements) / len(reform_history) if reform_history else 1.0
