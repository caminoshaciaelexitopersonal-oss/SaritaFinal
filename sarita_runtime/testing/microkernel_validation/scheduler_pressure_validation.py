import asyncio
import logging
import sys
import os

# Add root to path for imports
sys.path.append(os.getcwd())

from sarita_runtime.kernel.microkernel_fabric.sovereign_microkernel import SovereignMicrokernel
from sarita_runtime.kernel.scheduling_fabric.sovereign_cpu_scheduler import SovereignCPUScheduler
from sarita_runtime.kernel.memory_plane.memory_pressure_constitution import MemoryPressureConstitution

async def run_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Physical Microkernel Validation...")

    # 1. Microkernel Task Dispatch Validation
    mk = SovereignMicrokernel()
    await mk.boot()

    task_id = "test-task-001"
    payload = {"op": "RECONCILE", "provenance_token": "VALID-TOKEN-XYZ"}

    success = await mk.submit_task(task_id, payload, priority=0)
    if success:
        logging.info("Validation: Task submission SUCCESS.")
    else:
        logging.error("Validation: Task submission FAILED.")

    # 2. Scheduler Pressure Validation
    scheduler = SovereignCPUScheduler()
    psi = scheduler.get_psi_metrics()
    logging.info(f"Validation: PSI Metrics - {psi}")

    # 3. Memory Pressure Constitution Validation
    mem_const = MemoryPressureConstitution()
    strategy = await mem_const.evaluate_pressure_legitimacy(85.0)
    logging.info(f"Validation: Memory strategy for 85% pressure - {strategy}")

    logging.info("Physical Microkernel Validation COMPLETE.")

if __name__ == "__main__":
    asyncio.run(run_validation())
