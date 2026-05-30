import asyncio
import logging
import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.microkernel_fabric.sovereign_microkernel import SovereignMicrokernel
from sarita_runtime.kernel.clock_fabric.runtime_clock_authority import RuntimeClockAuthority

async def run_coherency_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Physical Runtime Coherency Validation...")

    mk = SovereignMicrokernel()
    await mk.boot()

    clock = RuntimeClockAuthority()
    ts1 = clock.get_time_ns()

    # Execution within a deterministic epoch
    await mk.epoch_orchestrator.initiate_execution_epoch(1, {"max_latency": 1.0})

    op = {"id": "COH-001", "type": "CACHE_FLUSH", "provenance_token": "SOV-1"}
    await mk.submit_task("COH-001", op)

    await mk.dispatcher.wait_for_completion("COH-001")

    ts2 = clock.get_time_ns()
    logging.info(f"Validation: Monotonic Clock Check - {ts2} > {ts1}: {ts2 > ts1}")

    await mk.epoch_orchestrator.seal_epoch(1)
    logging.info("Physical Runtime Coherency Validation COMPLETE.")

if __name__ == "__main__":
    asyncio.run(run_coherency_validation())
