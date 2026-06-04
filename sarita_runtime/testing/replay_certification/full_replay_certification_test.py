import unittest
import time
import os
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.sovereign_enforcement_fabric import SovereignEnforcementFabric
from sarita_runtime.kernel.runtime_replay_engine import RuntimeReplayEngine
from sarita_runtime.kernel.invariant_engine.runtime_invariant_engine import RuntimeInvariantEngine

class TestFullReplayCertification(unittest.TestCase):
    def test_reconstruction_equivalence(self):
        """MANDATORY: Replay 100% equivalent, Ledger isolated."""
        db_path = "/tmp/prod_ledger.db"
        if os.path.exists(db_path): os.remove(db_path)

        # 1. Original (Production)
        graph = UnifiedExecutionGraph(ledger_db=db_path)
        enforcement = SovereignEnforcementFabric(graph)
        enforcement.claim_hardware_path("NIC_1", 20, 1)
        graph.calculate_saturation({"cpu": 0.4, "memory": 0.6})

        graph.wait_for_convergence()

        # 2. Replay (Reconstruction)
        replay_engine = RuntimeReplayEngine(graph.ledger)
        replayed_graph = replay_engine.reconstruct_graph_state()

        replayed_graph.wait_for_convergence()

        # 3. Equivalence Certification
        invariant_engine = RuntimeInvariantEngine(graph)
        equivalent, details = invariant_engine.verify_replay_equivalence(replayed_graph)

        self.assertTrue(equivalent, f"Sovereign Divergence detected: {details}")
        self.assertEqual(graph.ownership, replayed_graph.ownership)

        # 4. Verify Isolation (Replay must not touch Prod Ledger)
        prod_count_before = graph.ledger.get_entry_count()
        replayed_graph.update_ownership("REPLAY_TOUCH", "INVALID")
        replayed_graph.wait_for_convergence()

        self.assertEqual(graph.ledger.get_entry_count(), prod_count_before, "Causal Contamination detected: Replay wrote to Production Ledger!")

        if os.path.exists(db_path): os.remove(db_path)

if __name__ == "__main__":
    unittest.main()
