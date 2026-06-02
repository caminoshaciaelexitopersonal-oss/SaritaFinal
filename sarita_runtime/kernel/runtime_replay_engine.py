import logging
import json
import sqlite3
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class RuntimeReplayEngine:
    """
    Sovereign Runtime Replay Engine (Phase 76).
    Reconstructs the system state from the material ledger.
    """
    def __init__(self, ledger):
        self.ledger = ledger

    def reconstruct_graph_state(self):
        logging.info("Replay Engine: Starting material state reconstruction.")

        # 1. Fetch all records from ledger
        conn = sqlite3.connect(self.ledger.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT actor, action, payload, decision_id, epoch FROM sovereign_ledger ORDER BY id ASC")
        records = cursor.fetchall()

        # 2. Replay into a fresh Graph
        replayed_graph = UnifiedExecutionGraph()

        for actor, action, payload_str, decision_id, epoch in records:
            payload = json.loads(payload_str)
            # Emit event to the new graph to reconstruct state
            replayed_graph.emit_event(actor, action, payload)

        conn.close()
        return replayed_graph
