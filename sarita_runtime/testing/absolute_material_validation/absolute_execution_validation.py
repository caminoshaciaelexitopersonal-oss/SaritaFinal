import asyncio
import logging
import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.microkernel_fabric.sovereign_microkernel import SovereignMicrokernel
from sarita_runtime.kernel.runtime_cortex.sovereign_runtime_cortex import SovereignRuntimeCortex

async def run_absolute_material_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Absolute Material Validation (Phase 72)...")

    # 1. Unified Cortex & Bus Initialization
    cortex = SovereignRuntimeCortex()
    cortex.boot_sovereign_cortex()

    # 2. Sovereign Bus (Execution Graph) Interaction
    task_id = "ABS-999"
    cortex.nervous_system.register_material_vertex(task_id, {"type": "ABSOLUTE_ENFORCEMENT"})
    cortex.nervous_system.update_physical_state("CPU-0", task_id)

    # 3. Material io_uring Task Submission
    mk = SovereignMicrokernel()
    await mk.boot()

    # Associate vertex with the dispatcher task
    mk.unified_authority.execution_graph = cortex.nervous_system

    success = await mk.submit_task(task_id, {"id": task_id, "type": "IO_URING_OP"})

    if success:
        logging.info(f"Validation: Absolute Material Task {task_id} Dispatched.")
    else:
        logging.error("Validation: Absolute Material Dispatch FAILED.")

    # 4. Memory Pressure Oracle Validation
    from sarita_runtime.kernel.memory_fabric.physical_memory_pressure_tracker import PhysicalMemoryPressureTracker
    tracker = PhysicalMemoryPressureTracker()
    logging.info(f"Validation: Physical PSI tracker active: {tracker.get_current_pressure()}")

    logging.info("Absolute Material Validation COMPLETE.")

if __name__ == "__main__":
    asyncio.run(run_absolute_material_validation())
