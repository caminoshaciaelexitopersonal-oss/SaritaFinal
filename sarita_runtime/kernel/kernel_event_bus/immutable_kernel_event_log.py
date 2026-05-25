import logging
import sqlite3
import json
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ImmutableKernelEventLog:
    """
    Persistent, append-only ledger for all kernel events.
    Uses ThreadPoolExecutor to prevent event loop starvation.
    """
    def __init__(self, db_path="/var/lib/sarita/kernel_events.db"):
        self.db_path = db_path
        self.executor = ThreadPoolExecutor(max_workers=1)
        self._init_db_sync()

    def _init_db_sync(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA journal_mode=WAL;")
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
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(self.executor, self._append_sync, event)

    def _append_sync(self, event: dict):
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute(
                "INSERT INTO kernel_events (id, type, payload, prev_hash, hash, epoch) VALUES (?, ?, ?, ?, ?, ?)",
                (event["id"], event["type"], json.dumps(event["payload"]), event["prev_hash"], event["hash"], event["epoch"])
            )
            conn.commit()
        finally:
            conn.close()

    async def get_events_from_epoch(self, epoch: int):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(self.executor, self._get_events_sync, epoch)

    def _get_events_sync(self, epoch: int):
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute("SELECT * FROM kernel_events WHERE epoch >= ? ORDER BY epoch ASC", (epoch,))
            return cursor.fetchall()
        finally:
            conn.close()
