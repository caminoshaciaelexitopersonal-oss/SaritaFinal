import unittest
import os
import time
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.runtime_replay_engine import RuntimeReplayEngine

class RestartRecoveryValidation(unittest.TestCase):
    def setUp(self):
        self.db_path = f"/tmp/restart_test_{int(time.time())}.db"

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_clean_shutdown_and_restart(self):
        # 1. Start original graph
        graph = UnifiedExecutionGraph(ledger_db=self.db_path)
        graph.emit_event("task_1", "OWNERSHIP_CHANGE", {"resource": "CPU_0", "owner": "task_1"})
        graph.emit_event("task_2", "PRESSURE_UPDATE", {"score": 0.5})
        graph.wait_for_convergence()

        original_ownership = dict(graph.ownership)
        original_pressure = graph.global_pressure

        # 2. Simulate shutdown (graph object destroyed)
        del graph

        # 3. Restart and Rehydrate
        # In a real restart, we use the ReplayEngine to rebuild the graph from the same DB
        from sarita_runtime.kernel.runtime_ledger.sovereign_audit_ledger import SovereignAuditLedger
        ledger = SovereignAuditLedger(self.db_path)
        replay_engine = RuntimeReplayEngine(ledger)
        restarted_graph = replay_engine.reconstruct_graph_state()
        restarted_graph.wait_for_convergence()

        self.assertEqual(original_ownership, restarted_graph.ownership)
        self.assertEqual(original_pressure, restarted_graph.global_pressure)

    def test_abrupt_shutdown_mid_load(self):
        graph = UnifiedExecutionGraph(ledger_db=self.db_path)
        for i in range(100):
            graph.emit_event(f"t_{i}", "TASK_AUTHORIZED", {"task": {"id": i}})

        # Do NOT wait for convergence, simulate abrupt stop
        # In practice, some events might be in the queue and not yet in the ledger
        # We want to verify that what DID make it to the ledger is consistent

        # Give it a tiny bit of time to process SOME events
        time.sleep(0.05)

        # 2. Simulate abrupt stop
        del graph

        # 3. Recovery
        from sarita_runtime.kernel.runtime_ledger.sovereign_audit_ledger import SovereignAuditLedger
        ledger = SovereignAuditLedger(self.db_path)
        replay_engine = RuntimeReplayEngine(ledger)
        recovered_graph = replay_engine.reconstruct_graph_state()
        recovered_graph.wait_for_convergence()

        # Verify ledger integrity
        is_valid, msg = ledger.verify_integrity()
        self.assertTrue(is_valid, f"Ledger corrupted after abrupt shutdown: {msg}")

        print(f"Recovered {len(recovered_graph.vertices)} vertices after abrupt shutdown.")

if __name__ == "__main__":
    unittest.main()
