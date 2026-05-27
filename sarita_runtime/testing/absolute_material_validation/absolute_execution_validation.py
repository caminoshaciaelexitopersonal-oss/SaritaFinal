import logging
import sys
import os
import threading

sys.path.append(os.getcwd())

from sarita_runtime.kernel.execution_fabric.sovereign_execution_kernel import SovereignExecutionKernel, DistributedExecutionRouter

def run_absolute_material_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Absolute Material Validation (Phase 72)...")

    # 1. Initialize material stack
    router = DistributedExecutionRouter()
    kernel = SovereignExecutionKernel(node_id="master-node", fabric_router=router)

    # 2. Boot physically (threaded)
    kernel.boot()

    # 3. Execution without asyncio/polling
    op = {
        "id": "ABS-TASK-72",
        "type": "MATERIAL_IO",
        "priority": 0,
        "provenance_token": "SOV-ABS-KEY"
    }

    logging.info("Validation: Executing material op via Unified Authority Chain...")
    # Add dummy entry to graph for validation
    kernel.microkernel.unified_authority.execution_graph.register_material_vertex("ABS-TASK-72", op)

    result = kernel.execute_material_op(op)

    if result and result.get("status") == "SUCCESS":
        logging.info("Validation: Absolute Material Execution SUCCESS.")
    else:
        logging.error(f"Validation: Absolute Material Execution FAILED. Result: {result}")

    logging.info("Absolute Material Validation COMPLETE.")

if __name__ == "__main__":
    run_absolute_material_validation()
