import time

class EvolutionSearchSpaceEngine:
    """
    Engine to reconstruct all viable evolutionary alternatives for a given decision.
    """
    def __init__(self, space_reconstructor, ledger):
        self.space_reconstructor = space_reconstructor
        self.ledger = ledger

    def map_evolutionary_search_space(self, decision_context, constraints):
        print(f"[EvolutionSearchSpaceEngine] Reconstructing search space for: {decision_context.get('id')}...")

        start_time = time.time()
        alternatives = self.space_reconstructor.generate_alternatives(decision_context, constraints)

        result = {
            "decision_id": decision_context.get("id"),
            "alternatives_discovered": len(alternatives),
            "search_space_density": len(alternatives) / 100.0,
            "execution_time": time.time() - start_time,
            "timestamp": time.time()
        }

        self.ledger.record_proof(result)
        return alternatives, result
