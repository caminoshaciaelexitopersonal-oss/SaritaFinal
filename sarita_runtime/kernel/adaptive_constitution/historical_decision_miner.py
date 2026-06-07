class HistoricalDecisionMiner:
    """
    Extracts relevant decision data from ledgers for analysis.
    """
    def mine_decisions(self, ledger):
        # Extract actions, triggers, and outcomes
        history = ledger.get_history()
        return [h for h in history if "action" in h]
