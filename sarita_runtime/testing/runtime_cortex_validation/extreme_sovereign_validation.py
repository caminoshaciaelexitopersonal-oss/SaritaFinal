import asyncio
import logging
import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.runtime_cortex.sovereign_runtime_cortex import SovereignRuntimeCortex
from sarita_runtime.kernel.microkernel_fabric.sovereign_microkernel import SovereignMicrokernel

async def run_sovereign_extreme_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Sovereign Extreme Physical Validation (Phase 71)...")

    # 1. Cortex Materialization
    cortex = SovereignRuntimeCortex()
    cortex.boot_sovereign_cortex()

    # 2. Nervous System & Vertex Resolution
    task_id = "SOV-TOTAL-001"
    vertex = cortex.nervous_system.register_material_execution(task_id, {"cpu": 0, "type": "TOTAL_SOVEREIGNTY"})

    # 3. Material io_uring Task
    mk = SovereignMicrokernel()
    await mk.boot()

    success = await mk.submit_task(task_id, {"id": task_id, "type": "IO_URING_OP"})

    if success:
        logging.info(f"Validation: Material task {task_id} dispatched via Cortex.")
    else:
        logging.error("Validation: Material dispatch FAILED.")

    # 4. Pressure Oracle Correlation
    from sarita_runtime.kernel.pressure_fabric.runtime_pressure_oracle import RuntimePressureOracle
    oracle = RuntimePressureOracle()
    oracle.update_oracle("IRQ", 0.95)
    sat = oracle.predict_global_saturation()
    logging.info(f"Validation: Oracle predicted saturation: {sat:.2f}")

    logging.info("Sovereign Extreme Physical Validation COMPLETE.")

if __name__ == "__main__":
    asyncio.run(run_sovereign_extreme_validation())
