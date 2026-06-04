import unittest
import time
import os
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.sovereign_enforcement_fabric import SovereignEnforcementFabric
from sarita_runtime.kernel.runtime_replay_engine import RuntimeReplayEngine
from sarita_runtime.kernel.causal_replay_validator import CausalReplayValidator
from sarita_runtime.kernel.invariant_engine.runtime_invariant_engine import RuntimeInvariantEngine

class TestReplayCertification(unittest.TestCase):
    def test_mathematical_equivalence(self):
        db_path = "/tmp/test_replay.db"
        if os.path.exists(db_path): os.remove(db_path)

        graph = UnifiedExecutionGraph(ledger_db=db_path)
        enforcement = SovereignEnforcementFabric(graph)
        enforcement.claim_hardware_path("NVME", 10, 2)
        graph.calculate_saturation({"cpu": 0.5})

        graph.wait_for_convergence()

        replay_engine = RuntimeReplayEngine(graph.ledger)
        replayed_graph = replay_engine.reconstruct_graph_state()

        replayed_graph.wait_for_convergence()

        valid, msg = CausalReplayValidator.validate_consistency(graph, replayed_graph)
        self.assertTrue(valid, f"State divergence: {msg}")

        invariant_engine = RuntimeInvariantEngine(replayed_graph)
        all_passed, details = invariant_engine.perform_full_audit()
        self.assertTrue(all_passed, f"Replayed invariants failed: {details}")

        if os.path.exists(db_path): os.remove(db_path)

if __name__ == "__main__":
    unittest.main()
