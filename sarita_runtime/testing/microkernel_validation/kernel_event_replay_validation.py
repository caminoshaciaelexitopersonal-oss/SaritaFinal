import asyncio
import logging
import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.kernel_event_bus.kernel_event_authority import KernelEventAuthority
from sarita_runtime.kernel.kernel_event_bus.immutable_kernel_event_log import ImmutableKernelEventLog

async def run_event_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Kernel Event Replay Validation...")

    log_path = "/tmp/validation_events.db"
    if os.path.exists(log_path):
        os.remove(log_path)
    authority = KernelEventAuthority(log_path=log_path)
    log = authority.log

    # Publish events
    for i in range(3):
        await authority.publish_event("KERNEL_BOOT_STEP", {"step": i})

    # Replay
    events = await log.get_events_from_epoch(0)
    logging.info(f"Validation: Replayed {len(events)} events from immutable log.")

    if len(events) == 3:
        logging.info("Validation: Event persistence and replay SUCCESS.")
    else:
        logging.error("Validation: Event persistence FAILED.")

if __name__ == "__main__":
    asyncio.run(run_event_validation())
