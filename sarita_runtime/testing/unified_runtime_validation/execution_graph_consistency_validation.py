import logging
import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.microkernel_fabric.sovereign_microkernel import SovereignMicrokernel
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

async def run_unified_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Unified Physical Runtime Validation (Phase 68)...")

    mk = SovereignMicrokernel()
    # Manual boost of graph for validation
    graph = mk.unified_authority.execution_graph

    task_id = "GRA-100"
    payload = {"id": task_id, "epoch": 1, "provenance_token": "SOV-KEY"}
    graph.add_execution_node(task_id, payload)

    await mk.boot()

    success = await mk.submit_task(task_id, payload)

    if success:
        logging.info("Validation: Unified Execution Graph Dispatch SUCCESS.")
    else:
        logging.error("Validation: Unified Execution Graph Dispatch FAILED.")

    logging.info("Unified Physical Runtime Validation COMPLETE.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_unified_validation())
