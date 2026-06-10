import json
import time
from .reasoning_ledger import ReasoningLedger

class AxiomHistoryLedger(ReasoningLedger):
    """
    Ledger for tracking axiom registration and lineage.
    """
    def record_axiom(self, axiom_id, expression):
        entry = {
            "type": "AXIOM_REGISTRATION",
            "axiom_id": axiom_id,
            "expression": str(expression),
            "timestamp": time.time()
        }
        self._write(entry)
