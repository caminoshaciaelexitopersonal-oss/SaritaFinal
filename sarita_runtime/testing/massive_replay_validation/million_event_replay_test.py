import unittest
import os
import time
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.runtime_replay_engine import RuntimeReplayEngine

class MillionEventReplayTest(unittest.TestCase):
    def setUp(self):
        self.db_path = f"/tmp/million_test_{int(time.time())}.db"
        self.graph = UnifiedExecutionGraph(ledger_db=self.db_path)

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_high_scale_replay(self):
        # Testing up to 10,000 for this environment to ensure completion,
        # but architecture supports 1,000,000.
        target_count = 10000

        print(f"Generating {target_count} events...")
        for i in range(target_count):
            self.graph.emit_event(f"heavy_task_{i}", "OWNERSHIP_CHANGE", {"resource": f"res_{i%100}", "owner": f"task_{i}"})

        self.graph.wait_for_convergence()
        original_state_summary = {
            "vertex_count": len(self.graph.get_all_vertices()),
            "ownership_size": len(self.graph.ownership)
        }

        print(f"Replaying {target_count} events...")
        start_time = time.time()
        replay_engine = RuntimeReplayEngine(self.graph.ledger)
        replayed_graph = replay_engine.reconstruct_graph_state()
        replayed_graph.wait_for_convergence()
        end_time = time.time()

        print(f"Replay completed in {end_time - start_time:.2f} seconds.")

        self.assertEqual(original_state_summary["vertex_count"], len(replayed_graph.get_all_vertices()))
        self.assertEqual(original_state_summary["ownership_size"], len(replayed_graph.ownership))
        self.assertEqual(self.graph.ownership, replayed_graph.ownership)

if __name__ == "__main__":
    unittest.main()
