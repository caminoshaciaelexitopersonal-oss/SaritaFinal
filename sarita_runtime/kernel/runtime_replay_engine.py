import logging
import json
import sqlite3
import os
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class RuntimeReplayEngine:
    def __init__(self, ledger):
        self.ledger = ledger

    def reconstruct_graph_state(self):
        logging.info("Replay Engine: Starting material state reconstruction.")

        conn = sqlite3.connect(self.ledger.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT actor, action, payload, decision_id, epoch FROM sovereign_ledger ORDER BY id ASC")
        records = cursor.fetchall()

        # Use a fresh temp DB for replayed graph to avoid interference and ensure table existence
        replayed_db = f"/tmp/replay_{os.getpid()}.db"
        if os.path.exists(replayed_db): os.remove(replayed_db)
        replayed_graph = UnifiedExecutionGraph(ledger_db=replayed_db)

        for actor, action, payload_str, decision_id, epoch in records:
            constitutional_evidence = json.loads(payload_str)
            replayed_graph.emit_event(actor, action, constitutional_evidence)

        conn.close()
        return replayed_graph
