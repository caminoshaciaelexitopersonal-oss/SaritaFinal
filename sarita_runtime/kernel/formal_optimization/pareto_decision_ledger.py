from .optimality_ledger import OptimalityLedger

class ParetoDecisionLedger(OptimalityLedger):
    """
    Ledger for recording Pareto-efficient decisions and tradeoff analysis.
    """
    def record_pareto_decision(self, decision_id, pareto_set, tradeoffs):
        entry = {
            "type": "PARETO_DECISION",
            "decision_id": decision_id,
            "pareto_set_size": len(pareto_set),
            "tradeoffs": tradeoffs,
            "timestamp": time.time()
        }
        self._write(entry)
