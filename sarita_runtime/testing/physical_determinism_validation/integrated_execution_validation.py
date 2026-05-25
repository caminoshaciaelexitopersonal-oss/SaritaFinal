import asyncio
import logging
import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.execution_fabric.sovereign_execution_kernel import SovereignExecutionKernel, DistributedExecutionRouter

async def run_integrated_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Integrated Physical Validation (Phase 63/64)...")

    router = DistributedExecutionRouter()
    kernel = SovereignExecutionKernel(node_id="node-master", fabric_router=router)

    await kernel.boot()

    # Material execution via Microkernel delegation
    op = {
        "id": "OP-777",
        "type": "LEDGER_SYNC",
        "priority": 0,
        "provenance_token": "SOVEREIGN-KEY-123"
    }

    logging.info("Validation: Executing federated op via Sovereign Microkernel...")
    result = await kernel.execute_federated_op(op)

    if result and result.get("status") == "SUCCESS" and result.get("op_id") == "OP-777":
        logging.info("Validation: Integrated Execution SUCCESS.")
    else:
        logging.error(f"Validation: Integrated Execution FAILED. Result: {result}")

    logging.info("Integrated Physical Validation COMPLETE.")

if __name__ == "__main__":
    asyncio.run(run_integrated_validation())
