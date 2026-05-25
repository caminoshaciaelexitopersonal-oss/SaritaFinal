import logging
import hashlib
import time
import json
from typing import Dict, Any
from sarita_runtime.kernel.kernel_event_bus.immutable_kernel_event_log import ImmutableKernelEventLog

class KernelEventAuthority:
    """
    Eliminates event fragmentation. Monotonic authority for all kernel events.
    """
    def __init__(self, log_path="/var/lib/sarita/kernel_events.db"):
        self.current_epoch = 0
        self.last_event_hash = "0" * 64
        self.log = ImmutableKernelEventLog(log_path)

    async def publish_event(self, event_type: str, payload: Dict[str, Any]):
        logging.info(f"Kernel Event Authority: Publishing {event_type} (Epoch: {self.current_epoch})")

        event_id = f"{self.current_epoch}-{int(time.time()*1000)}"
        event_hash = self._calculate_event_hash(event_id, event_type, payload)

        event = {
            "id": event_id,
            "type": event_type,
            "payload": payload,
            "prev_hash": self.last_event_hash,
            "hash": event_hash,
            "epoch": self.current_epoch
        }

        await self.log.append(event)

        self.last_event_hash = event_hash
        self.current_epoch += 1
        return event

    def _calculate_event_hash(self, event_id, event_type, payload):
        payload_str = json.dumps(payload, sort_keys=True)
        data = f"{event_id}{event_type}{payload_str}{self.last_event_hash}"
        return hashlib.sha256(data.encode()).hexdigest()
