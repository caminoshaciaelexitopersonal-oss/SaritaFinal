import unittest
import os
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.non_divergence_validator import NonDivergenceValidator

class NonDivergenceTest(unittest.TestCase):
    def test_production_replay_alignment(self):
        db_path = "/tmp/divergence_check.db"
        if os.path.exists(db_path): os.remove(db_path)

        graph = UnifiedExecutionGraph(ledger_db=db_path)

        # Simulate complex workload
        graph.emit_event("t1", "OWNERSHIP_CHANGE", {"resource": "GPU_0", "owner": "t1"})
        graph.emit_event("t2", "PRESSURE_UPDATE", {"score": 0.75})
        graph.emit_event("t1", "EXECUTION_COMPLETE", {})
        graph.emit_event("t3", "SET_NUMA_AFFINITY", {"node": 1})

        is_certified, results = NonDivergenceValidator.validate(graph)

        print(f"Non-Divergence Results: {results}")
        self.assertTrue(is_certified, f"Divergence detected: {results}")

        if os.path.exists(db_path): os.remove(db_path)

if __name__ == "__main__":
    unittest.main()
