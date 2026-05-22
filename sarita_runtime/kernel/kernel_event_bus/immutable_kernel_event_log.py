import logging
import sqlite3
import json
import os

class ImmutableKernelEventLog:
    """
    Persistent, append-only ledger for all kernel events.
    """
    def __init__(self, db_path="/tmp/sarita_kernel_events.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS kernel_events (
                id TEXT PRIMARY KEY,
                type TEXT,
                payload TEXT,
                prev_hash TEXT,
                hash TEXT,
                epoch INTEGER,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

    async def append(self, event: dict):
        logging.info(f"Kernel Log: Appending event {event['id']} to immutable storage.")
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO kernel_events (id, type, payload, prev_hash, hash, epoch) VALUES (?, ?, ?, ?, ?, ?)",
            (event["id"], event["type"], json.dumps(event["payload"]), event["prev_hash"], event["hash"], event["epoch"])
        )
        conn.commit()
        conn.close()

    async def get_events_from_epoch(self, epoch: int):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute("SELECT * FROM kernel_events WHERE epoch >= ? ORDER BY epoch ASC", (epoch,))
        events = cursor.fetchall()
        conn.close()
        return events
