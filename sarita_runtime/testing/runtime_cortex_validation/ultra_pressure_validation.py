import asyncio
import logging
import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.microkernel_fabric.sovereign_microkernel import SovereignMicrokernel
from sarita_runtime.kernel.runtime_cortex.sovereign_runtime_cortex import SovereignRuntimeCortex
from sarita_runtime.kernel.scheduler_fabric.deterministic_runtime_scheduler import DeterministicRuntimeScheduler

async def run_ultra_pressure_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Ultra-Pressure Physical Validation (Phase 70)...")

    # 1. Cortex Initialization
    cortex = SovereignRuntimeCortex()
    cortex.boot_cortex()

    # 2. Scheduler Materialization
    scheduler = DeterministicRuntimeScheduler(cortex.nervous_system)

    # 3. Simulate Pressure Signal
    cortex.process_physical_signal("IO_SUBSYSTEM", "PRESSURE_SPIKE", {"score": 0.95})

    # 4. Task Scheduling under Pressure
    task_id = "URGENT-001"
    scheduler.schedule_task(task_id, deadline_ns=1000000)

    logging.info(f"Validation: Task {task_id} scheduled in cortex context.")
    logging.info(f"Validation: Global pressure score: {cortex.nervous_system.global_pressure_score}")

    logging.info("Ultra-Pressure Physical Validation COMPLETE.")

if __name__ == "__main__":
    asyncio.run(run_ultra_pressure_validation())
