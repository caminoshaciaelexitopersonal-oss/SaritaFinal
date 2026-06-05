import unittest
import os
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.runtime_replay_engine import RuntimeReplayEngine

class HashChainEquivalenceTest(unittest.TestCase):
    def test_hash_chain_consistency(self):
        db_path = "/tmp/hash_chain.db"
        if os.path.exists(db_path): os.remove(db_path)

        graph = UnifiedExecutionGraph(ledger_db=db_path)

        # Create a chain of events
        graph.emit_event("t1", "ACTION_A", {"data": 1})
        graph.emit_event("t2", "ACTION_B", {"data": 2})
        graph.emit_event("t3", "ACTION_C", {"data": 3})

        graph.wait_for_convergence()

        original_vertices = graph.get_all_vertices()

        # Check original chain linkage
        for i in range(1, len(original_vertices)):
            self.assertEqual(original_vertices[i].payload['parent_hash'], original_vertices[i-1].vertex_hash)

        # Replay
        replay_engine = RuntimeReplayEngine(graph.ledger)
        replayed_graph = replay_engine.reconstruct_graph_state()
        replayed_graph.wait_for_convergence()

        replayed_vertices = replayed_graph.get_all_vertices()

        # Verify replayed chain linkage
        for i in range(len(original_vertices)):
            self.assertEqual(original_vertices[i].vertex_hash, replayed_vertices[i].vertex_hash)
            if i > 0:
                self.assertEqual(replayed_vertices[i].payload['parent_hash'], replayed_vertices[i-1].vertex_hash)

        if os.path.exists(db_path): os.remove(db_path)

if __name__ == "__main__":
    unittest.main()
