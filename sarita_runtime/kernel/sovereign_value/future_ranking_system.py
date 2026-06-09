class FutureRankingSystem:
    """
    Ranks projected futures based on value, stability, and survival.
    """
    def rank_futures(self, futures: list):
        # Sort by stability DESC, risk ASC
        ranked = sorted(futures, key=lambda x: (x["stability"], -x["risk"]), reverse=True)
        return ranked
