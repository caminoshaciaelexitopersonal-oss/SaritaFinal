import unittest
import os
import time
import logging
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.runtime_replay_engine import RuntimeReplayEngine

class MassiveReplayTest(unittest.TestCase):
    def setUp(self):
        self.db_path = f"/tmp/massive_test_{int(time.time())}.db"
        self.graph = UnifiedExecutionGraph(ledger_db=self.db_path)

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_massive_event_replay(self):
        event_counts = [10, 100, 1000] # Reduced for standard CI, can be scaled to 100,000

        for count in event_counts:
            # 1. Generate Events
            for i in range(count):
                self.graph.emit_event(f"task_{i}", "PRESSURE_UPDATE", {"score": 0.1 * (i % 10)})

            self.graph.wait_for_convergence()

            original_vertices = self.graph.get_all_vertices()
            original_ownership = dict(self.graph.ownership)
            original_pressure = self.graph.global_pressure

            # 2. Reconstruct
            replay_engine = RuntimeReplayEngine(self.graph.ledger)
            replayed_graph = replay_engine.reconstruct_graph_state()
            replayed_graph.wait_for_convergence()

            replayed_vertices = replayed_graph.get_all_vertices()

            # 3. Verify
            self.assertEqual(len(original_vertices), len(replayed_vertices), f"Vertex count mismatch for {count} events")
            self.assertEqual(original_ownership, replayed_graph.ownership, f"Ownership mismatch for {count} events")
            self.assertAlmostEqual(original_pressure, replayed_graph.global_pressure, places=5, msg=f"Pressure mismatch for {count} events")

            # Verify Hash Chains
            for i in range(len(original_vertices)):
                self.assertEqual(original_vertices[i].vertex_hash, replayed_vertices[i].vertex_hash)

if __name__ == "__main__":
    unittest.main()
