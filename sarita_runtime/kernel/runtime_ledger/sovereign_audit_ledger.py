import sqlite3
import hashlib
import time
import logging
import os
import json

class SovereignAuditLedger:
    """
    Consolidated Sovereign Ledger (Phase 73/76/77).
    """
    def __init__(self, db_path: str = "/tmp/sarita_ledger.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        if self.db_path != ":memory:":
            try:
                os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            except Exception:
                pass

        conn = sqlite3.connect(self.db_path)
        # Enable WAL mode for better concurrency and ensure table is committed
        conn.execute("PRAGMA journal_mode=WAL")
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
        # Ensure WAL mode and sync for deterministic writes
        conn.execute("PRAGMA journal_mode=WAL")
        cursor = conn.cursor()

        cursor.execute("SELECT entry_hash FROM sovereign_ledger ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        prev_hash = row[0] if row else "0" * 64

        timestamp = time.time()
        raw_data = f"{actor}:{action}:{payload}:{prev_hash}:{timestamp}:{decision_id}:{epoch}"
        entry_hash = hashlib.sha256(raw_data.encode()).hexdigest()

        cursor.execute("""
            INSERT INTO sovereign_ledger (actor, action, payload, prev_hash, entry_hash, timestamp, decision_id, epoch)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (actor, action, payload, prev_hash, entry_hash, timestamp, decision_id, epoch))

        conn.commit()
        conn.close()
        return entry_hash

    def record_vertex(self, vertex):
        return self.record_entry(
            actor=vertex.task_id,
            action=vertex.payload.get('action', 'UNKNOWN'),
            payload=json.dumps(vertex.payload, sort_keys=True),
            decision_id=vertex.vertex_id,
            epoch=vertex.execution_epoch
        )

    def record_vertices_batch(self, vertices):
        """Records multiple vertices in a single transaction for high performance."""
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.execute("BEGIN TRANSACTION")

        cursor = conn.cursor()

        # Get last hash for the start of the batch
        cursor.execute("SELECT entry_hash FROM sovereign_ledger ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        prev_hash = row[0] if row else "0" * 64

        for vertex in vertices:
            actor = vertex.task_id
            action = vertex.payload.get('action', 'UNKNOWN')
            payload = json.dumps(vertex.payload, sort_keys=True)
            decision_id = vertex.vertex_id
            epoch = vertex.execution_epoch
            timestamp = time.time()

            raw_data = f"{actor}:{action}:{payload}:{prev_hash}:{timestamp}:{decision_id}:{epoch}"
            entry_hash = hashlib.sha256(raw_data.encode()).hexdigest()

            cursor.execute("""
                INSERT INTO sovereign_ledger (actor, action, payload, prev_hash, entry_hash, timestamp, decision_id, epoch)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (actor, action, payload, prev_hash, entry_hash, timestamp, decision_id, epoch))

            prev_hash = entry_hash

        conn.commit()
        conn.close()

    def verify_integrity(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, actor, action, payload, prev_hash, entry_hash, timestamp, decision_id, epoch FROM sovereign_ledger ORDER BY id ASC")
        rows = cursor.fetchall()

        expected_prev = "0" * 64
        for row in rows:
            rid, actor, action, payload, prev_hash, entry_hash, timestamp, decision_id, epoch = row
            if prev_hash != expected_prev:
                conn.close()
                return False, f"Integrity violation at ID {rid}"

            raw_data = f"{actor}:{action}:{payload}:{prev_hash}:{timestamp}:{decision_id}:{epoch}"
            calc_hash = hashlib.sha256(raw_data.encode()).hexdigest()
            if calc_hash != entry_hash:
                conn.close()
                return False, f"Hash mismatch at ID {rid}"

            expected_prev = entry_hash

        conn.close()
        return True, "LEDGER_INTEGRITY_VERIFIED"

    def get_entry_count(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM sovereign_ledger")
        count = cursor.fetchone()[0]
        conn.close()
        return count
