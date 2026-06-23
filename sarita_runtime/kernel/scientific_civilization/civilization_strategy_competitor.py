class CivilizationStrategyCompetitor:
    def compete(self, strategies):
        # Compares strategies based on discovery ROI
        return sorted(strategies, key=lambda s: s.get("roi", 0), reverse=True)
