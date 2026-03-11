import logging
import json
from datetime import timezone, datetime

logger = logging.getLogger(__name__)

class OperationalMemory:
    """MEMORIA OPERATIVA DE AGENTES"""
    def __init__(self):
        self.events = []

    async def save_event(self, domain, event_type, payload, outcome):
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "domain": domain,
            "event_type": event_type,
            "data": payload,
            "outcome": outcome
        }
        self.events.append(event)
        return True

    async def retrieve_context(self, query):
        return [e for e in self.events if query in e['domain']][-5:]

memory_store = OperationalMemory()
