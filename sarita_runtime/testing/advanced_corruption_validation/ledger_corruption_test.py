import unittest
import sqlite3
import os
import time
from sarita_runtime.kernel.runtime_ledger.sovereign_audit_ledger import SovereignAuditLedger

class LedgerCorruptionTest(unittest.TestCase):
    def setUp(self):
        self.db_path = f"/tmp/corruption_test_{int(time.time())}.db"
        self.ledger = SovereignAuditLedger(self.db_path)
        # Populate
        for i in range(5):
            self.ledger.record_entry(f"task_{i}", "ACTION", f"payload_{i}")

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_detect_hash_mismatch(self):
        # Verify initial integrity
        is_valid, _ = self.ledger.verify_integrity()
        self.assertTrue(is_valid)

        # Corrupt a payload in the database
        conn = sqlite3.connect(self.db_path)
        conn.execute("UPDATE sovereign_ledger SET payload = 'CORRUPTED' WHERE id = 3")
        conn.commit()
        conn.close()

        # Verify detection
        is_valid, msg = self.ledger.verify_integrity()
        self.assertFalse(is_valid)
        self.assertIn("Hash mismatch at ID 3", msg)

    def test_detect_chain_break(self):
        # Corrupt a prev_hash
        conn = sqlite3.connect(self.db_path)
        conn.execute("UPDATE sovereign_ledger SET prev_hash = 'BROKEN' WHERE id = 4")
        conn.commit()
        conn.close()

        is_valid, msg = self.ledger.verify_integrity()
        self.assertFalse(is_valid)
        self.assertIn("Integrity violation at ID 4", msg)

if __name__ == "__main__":
    unittest.main()
