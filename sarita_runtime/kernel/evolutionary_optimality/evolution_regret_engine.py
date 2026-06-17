import time

class EvolutionRegretEngine:
    """
    Engine to compute Regret Score, Opportunity Loss, and Missed Benefits.
    """
    def __init__(self, ledger):
        self.ledger = ledger

    def calculate_evolution_regret(self, selected_outcome, counterfactual_results):
        print("[EvolutionRegretEngine] Quantifying evolutionary regret...")

        max_fitness = max([r.get("projected_fitness", 0.0) for r in counterfactual_results]) if counterfactual_results else 1.0
        selected_fitness = selected_outcome.get("fitness", 0.85)

        opportunity_loss = max(0.0, max_fitness - selected_fitness)
        regret_score = 1.0 - opportunity_loss

        result = {
            "regret_score": round(regret_score, 4),
            "opportunity_loss": round(opportunity_loss, 4),
            "missed_benefit": round(opportunity_loss * 1.5, 4),
            "timestamp": time.time()
        }

        self.ledger.record_proof(result)
        return result
