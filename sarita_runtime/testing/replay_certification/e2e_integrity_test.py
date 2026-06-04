import unittest
import time
import os
from sarita_runtime.kernel.runtime_cortex.sovereign_cortex import SovereignCortex
from sarita_runtime.kernel.sovereign_enforcement_fabric import SovereignEnforcementFabric
from sarita_runtime.kernel.runtime_replay_engine import RuntimeReplayEngine
from sarita_runtime.kernel.invariant_engine.runtime_invariant_engine import RuntimeInvariantEngine

class TestEndToEndIntegrity(unittest.TestCase):
    def test_full_chain_integrity(self):
        """Telemetry -> Graph -> Hardware -> Ledger -> Replay -> Verification"""
        db = "/tmp/e2e.db"
        if os.path.exists(db): os.remove(db)

        # 1. Setup
        cortex = SovereignCortex()
        graph = cortex.nervous_system
        graph.ledger.db_path = db
        graph.ledger._init_db()
        enforcement = SovereignEnforcementFabric(graph)

        # 2. Activity
        cortex.process_telemetry_signal("thermal", "TEMPERATURE", 0.95)
        enforcement.claim_hardware_path("NIC", 15, 0)
        enforcement.execute_material_io("task_e2e", "WRITE", {"fd": 1})

        graph.wait_for_convergence()

        # 3. Verification
        inv_engine = RuntimeInvariantEngine(graph)
        passed, details = inv_engine.perform_full_audit()
        self.assertTrue(passed, details)

        # 4. Replay
        replay_engine = RuntimeReplayEngine(graph.ledger)
        replayed_graph = replay_engine.reconstruct_graph_state()
        replayed_graph.wait_for_convergence()

        # 5. Final Equivalence
        equivalent, eq_details = inv_engine.verify_replay_equivalence(replayed_graph)
        self.assertTrue(equivalent, eq_details)

        if os.path.exists(db): os.remove(db)

if __name__ == "__main__":
    unittest.main()
