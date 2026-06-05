import unittest
import os
import sqlite3
import time
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.runtime_replay_engine import RuntimeReplayEngine

class ExtremeRecoveryTest(unittest.TestCase):
    def setUp(self):
        self.db_path = f"/tmp/extreme_recovery_{int(time.time())}.db"

    def tearDown(self):
        if os.path.exists(self.db_path): os.remove(self.db_path)

    def test_repeated_abrupt_shutdown(self):
        # 1. Start graph and flood
        for run in range(3):
            graph = UnifiedExecutionGraph(ledger_db=self.db_path)
            for i in range(100):
                graph.emit_event(f"run_{run}_t_{i}", "LOAD", {"v": i})

            # Abrupt stop (no wait)
            time.sleep(0.05)
            graph.shutdown() # In this simulation, we use shutdown but don't wait for queue to empty

        # 2. Reconstruct
        from sarita_runtime.kernel.runtime_ledger.sovereign_audit_ledger import SovereignAuditLedger
        ledger = SovereignAuditLedger(self.db_path)
        replay_engine = RuntimeReplayEngine(ledger)
        replayed_graph = replay_engine.reconstruct_graph_state()
        replayed_graph.wait_for_convergence()

        # 3. Verify Ledger Integrity
        is_valid, msg = ledger.verify_integrity()
        self.assertTrue(is_valid, f"Ledger corrupted after repeated shutdowns: {msg}")
        print(f"Recovered {len(replayed_graph.vertices)} total vertices after 3 crash cycles.")

if __name__ == "__main__":
    unittest.main()
