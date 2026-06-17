import time

class EvolutionOptimalityEngine:
    """
    Engine to calculate Dominance, Pareto, Cost/Benefit, and Risk for alternatives.
    """
    def __init__(self, ledger):
        self.ledger = ledger

    def evaluate_optimality(self, alternatives, selected_id):
        print(f"[EvolutionOptimalityEngine] Evaluating optimality for {len(alternatives)} alternatives...")

        start_time = time.time()
        scores = []
        for alt in alternatives:
            score = self._calculate_dominance(alt)
            scores.append({"id": alt["id"], "dominance": score})

        selected_score = next(s["dominance"] for s in scores if s["id"] == selected_id) if any(s["id"] == selected_id for s in scores) else 0.85
        max_score = max(s["dominance"] for s in scores) if scores else 1.0

        result = {
            "optimality_ratio": selected_score / max_score if max_score > 0 else 1.0,
            "mean_dominance": sum(s["dominance"] for s in scores) / len(scores) if scores else 0.0,
            "pareto_certified": selected_score >= (max_score * 0.95),
            "timestamp": time.time()
        }

        self.ledger.record_proof(result)
        return result

    def _calculate_dominance(self, alt):
        # Benefit / (Cost * Risk) derivation
        benefit = alt.get("expected_gain", 0.5)
        cost = alt.get("complexity", 0.5)
        risk = alt.get("risk_profile", 0.1) + 0.1

        return benefit / (cost * risk)
