import unittest
import sqlite3
import time
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.runtime_ledger.sovereign_audit_ledger import SovereignAuditLedger
from sarita_runtime.kernel.invariant_engine.runtime_invariant_engine import RuntimeInvariantEngine

class TestLedgerCorruption(unittest.TestCase):
    def test_hash_tampering_detection(self):
        """Demuestra la detección inmediata de alteración de hashes en el Ledger."""
        graph = UnifiedExecutionGraph(ledger_db="tamper.db")
        graph.update_ownership("DISK", "0")
        time.sleep(0.5)

        # Simular corrupción manual del DB
        conn = sqlite3.connect("tamper.db")
        conn.execute("UPDATE sovereign_ledger SET entry_hash = 'corrupted' WHERE id = 1")
        conn.commit()
        conn.close()

        # Verificar detección
        valid, msg = graph.ledger.verify_integrity()
        self.assertFalse(valid)
        self.assertIn("Hash mismatch", msg)

    def test_causal_break_detection(self):
        """Demuestra la detección de ruptura en la cadena causal (prev_hash)."""
        graph = UnifiedExecutionGraph(ledger_db="break.db")
        graph.update_ownership("DISK", "0")
        time.sleep(0.5)

        conn = sqlite3.connect("break.db")
        conn.execute("UPDATE sovereign_ledger SET prev_hash = 'invalid' WHERE id = 1")
        conn.commit()
        conn.close()

        valid, msg = graph.ledger.verify_integrity()
        self.assertFalse(valid)
        self.assertIn("Integrity violation", msg)

if __name__ == "__main__":
    unittest.main()
