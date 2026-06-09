from .adaptive_evolution_ledger import AdaptiveEvolutionLedger

class StressTestLedger(AdaptiveEvolutionLedger):
    """
    Ledger for recording results of evolutionary stress testing.
    """
    def record_stress_results(self, constitution_id, results):
        self._write({
            "type": "STRESS_TEST_RESULTS",
            "constitution_id": constitution_id,
            "scenarios_count": len(results),
            "all_resilient": all(r["is_resilient"] for r in results)
        })
