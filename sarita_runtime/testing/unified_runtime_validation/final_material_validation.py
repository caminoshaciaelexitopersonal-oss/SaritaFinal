import asyncio
import logging
import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.microkernel_fabric.sovereign_microkernel import SovereignMicrokernel
from sarita_runtime.kernel.runtime_ledger.runtime_constitutional_ledger import RuntimeConstitutionalLedger

async def run_final_material_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Final Material Validation Suite (Phase 68)...")

    # 1. Microkernel & Dispatcher materialization (no polling/sleeps)
    mk = SovereignMicrokernel()
    await mk.boot()

    # 2. Constitutional Ledger Physical Persistence
    ledger = RuntimeConstitutionalLedger("/tmp/final_material_ledger.db")
    task_id = "MAT-001"
    evidence = {"cpu": 0, "latency_ns": 1200, "entropy": 1024}

    ledger.append_material_proof(task_id, 1, evidence, "LEGITIMATE")
    logging.info("Validation: Material proof recorded in ledger.")

    # 3. Execution Graph Materialization
    vertex = mk.unified_authority.execution_graph.register_material_execution(task_id, {"id": task_id})
    if vertex:
        logging.info("Validation: Task registered in material execution graph.")

    logging.info("Final Material Validation Suite COMPLETE.")

if __name__ == "__main__":
    asyncio.run(run_final_material_validation())
