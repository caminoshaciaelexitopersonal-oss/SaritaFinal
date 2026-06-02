import sqlite3
import hashlib
import time
import logging
import os
import json

class SovereignAuditLedger:
    """
    Consolidated Sovereign Ledger (Phase 73/76).
    REFACTORED PHASE 76: Support for deep vertex evidence and decision_id.
    """
    def __init__(self, db_path: str = "/var/lib/sarita/runtime_ledger.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        try:
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        except Exception:
            self.db_path = "runtime_ledger.db"

        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=EXTRA")

        conn.execute("""
            CREATE TABLE IF NOT EXISTS sovereign_ledger (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                actor TEXT,
                action TEXT,
                payload TEXT,
                prev_hash TEXT,
                entry_hash TEXT,
                timestamp REAL,
                decision_id TEXT,
                epoch INTEGER
            )
        """)
        conn.commit()
        conn.close()

    def record_entry(self, actor: str, action: str, payload: str, decision_id: str = None, epoch: int = 0):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT entry_hash FROM sovereign_ledger ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        prev_hash = row[0] if row else "0" * 64

        timestamp = time.time()
        # Richer raw data for Phase 76
        raw_data = f"{actor}:{action}:{payload}:{prev_hash}:{timestamp}:{decision_id}:{epoch}"
        entry_hash = hashlib.sha256(raw_data.encode()).hexdigest()

        cursor.execute("""
            INSERT INTO sovereign_ledger (actor, action, payload, prev_hash, entry_hash, timestamp, decision_id, epoch)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (actor, action, payload, prev_hash, entry_hash, timestamp, decision_id, epoch))

        conn.commit()
        conn.close()
        logging.info(f"Ledger: Committed material evidence {entry_hash[:8]} (Decision: {decision_id})")
        return entry_hash

    def record_vertex(self, vertex):
        """Materializes a Graph Vertex directly into the Ledger."""
        return self.record_entry(
            actor=vertex.task_id,
            action=vertex.payload.get('action', 'UNKNOWN'),
            payload=json.dumps(vertex.payload),
            decision_id=vertex.vertex_id,
            epoch=vertex.execution_epoch
        )

    def verify_integrity(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, actor, action, payload, prev_hash, entry_hash, timestamp, decision_id, epoch FROM sovereign_ledger ORDER BY id ASC")
        rows = cursor.fetchall()

        expected_prev = "0" * 64
        for row in rows:
            rid, actor, action, payload, prev_hash, entry_hash, timestamp, decision_id, epoch = row
            if prev_hash != expected_prev:
                return False, f"Integrity violation at ID {rid}"

            raw_data = f"{actor}:{action}:{payload}:{prev_hash}:{timestamp}:{decision_id}:{epoch}"
            calc_hash = hashlib.sha256(raw_data.encode()).hexdigest()
            if calc_hash != entry_hash:
                return False, f"Hash mismatch at ID {rid}"

            expected_prev = entry_hash

        conn.close()
        return True, "LEDGER_INTEGRITY_VERIFIED"
