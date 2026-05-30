import sqlite3
import hashlib
import time
import logging
import os

class SovereignAuditLedger:
    """
    Consolidated Sovereign Ledger (Phase 73).
    Single Authority for Immutable Operational Evidence.
    Mandates WAL mode and chained causal hashing.
    """
    def __init__(self, db_path: str = "/var/lib/sarita/runtime_ledger.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        try:
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        except Exception:
            self.db_path = "runtime_ledger.db" # Fallback to local

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
                timestamp REAL
            )
        """)
        conn.commit()
        conn.close()

    def record_entry(self, actor: str, action: str, payload: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # 1. Get previous hash
        cursor.execute("SELECT entry_hash FROM sovereign_ledger ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        prev_hash = row[0] if row else "0" * 64

        # 2. Calculate current hash
        timestamp = time.time()
        raw_data = f"{actor}:{action}:{payload}:{prev_hash}:{timestamp}"
        entry_hash = hashlib.sha256(raw_data.encode()).hexdigest()

        # 3. Commit
        cursor.execute("""
            INSERT INTO sovereign_ledger (actor, action, payload, prev_hash, entry_hash, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (actor, action, payload, prev_hash, entry_hash, timestamp))

        conn.commit()
        conn.close()
        logging.info(f"Ledger: Committed audit entry {entry_hash[:8]} for {actor}")
        return entry_hash

    def verify_integrity(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, actor, action, payload, prev_hash, entry_hash, timestamp FROM sovereign_ledger ORDER BY id ASC")
        rows = cursor.fetchall()

        expected_prev = "0" * 64
        for row in rows:
            rid, actor, action, payload, prev_hash, entry_hash, timestamp = row
            if prev_hash != expected_prev:
                return False, f"Integrity violation at ID {rid}"

            raw_data = f"{actor}:{action}:{payload}:{prev_hash}:{timestamp}"
            calc_hash = hashlib.sha256(raw_data.encode()).hexdigest()
            if calc_hash != entry_hash:
                return False, f"Hash mismatch at ID {rid}"

            expected_prev = entry_hash

        conn.close()
        return True, "LEDGER_INTEGRITY_VERIFIED"
