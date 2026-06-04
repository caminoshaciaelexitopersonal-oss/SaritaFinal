import unittest
import os
import time
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.non_divergence_validator import NonDivergenceValidator

class LargeScaleNonDivergenceTest(unittest.TestCase):
    def test_high_volume_non_divergence(self):
        # Using 10,000 for standard validation to ensure completion in the environment
        db_path = f"/tmp/large_divergence_{int(time.time())}.db"
        if os.path.exists(db_path): os.remove(db_path)

        graph = UnifiedExecutionGraph(ledger_db=db_path)
        count = 10000

        print(f"Generating {count} events for non-divergence check...")
        for i in range(count):
            if i % 3 == 0:
                graph.emit_event(f"t_{i}", "OWNERSHIP_CHANGE", {"resource": f"res_{i%10}", "owner": f"t_{i}"})
            elif i % 3 == 1:
                graph.emit_event(f"t_{i}", "PRESSURE_UPDATE", {"score": (i % 100) / 100.0})
            else:
                graph.emit_event(f"t_{i}", "SET_NUMA_AFFINITY", {"node": i % 4})

        is_certified, results = NonDivergenceValidator.validate(graph)

        print(f"Non-Divergence Results: {results}")
        self.assertTrue(is_certified)

        graph.shutdown()
        if os.path.exists(db_path): os.remove(db_path)

if __name__ == "__main__":
    unittest.main()
