from .adaptive_evolution_ledger import AdaptiveEvolutionLedger

class DominanceHistoryLedger(AdaptiveEvolutionLedger):
    """
    Ledger for recording longitudinal dominance and survival forecasts.
    """
    def record_dominance_forecast(self, result):
        self._write({
            "type": "DOMINANCE_FORECAST",
            "generations": result["generations"],
            "winner_id": result["winner"],
            "forecast_count": len(result["forecasts"])
        })
