import unittest
import os
import sqlite3
import time
from sarita_runtime.kernel.runtime_ledger.sovereign_audit_ledger import SovereignAuditLedger

class LedgerSaturationTest(unittest.TestCase):
    def setUp(self):
        self.db_path = f"/tmp/saturation_{int(time.time())}.db"
        self.ledger = SovereignAuditLedger(self.db_path)

    def tearDown(self):
        if os.path.exists(self.db_path): os.remove(self.db_path)

    def test_wal_mode_and_saturation(self):
        # Verify WAL mode
        conn = sqlite3.connect(self.db_path)
        mode = conn.execute("PRAGMA journal_mode").fetchone()[0]
        conn.close()
        self.assertEqual(mode.lower(), "wal")

        # Flood ledger with entries
        batch_count = 10
        events_per_batch = 1000
        for i in range(batch_count):
            batch = []
            for j in range(events_per_batch):
                class FakeVertex:
                    def __init__(self, idx):
                        self.task_id = f"t_{idx}"
                        self.payload = {"action": "SATURATION_TEST", "val": idx}
                        self.vertex_id = f"v_{idx}"
                        self.execution_epoch = 0
                batch.append(FakeVertex(i * events_per_batch + j))
            self.ledger.record_vertices_batch(batch)

        # Verify count
        self.assertEqual(self.ledger.get_entry_count(), batch_count * events_per_batch)

        # Verify Integrity under saturation
        is_valid, msg = self.ledger.verify_integrity()
        self.assertTrue(is_valid, f"Integrity failed: {msg}")

if __name__ == "__main__":
    unittest.main()
