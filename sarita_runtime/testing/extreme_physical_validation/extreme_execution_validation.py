import asyncio
import logging
import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.microkernel_fabric.sovereign_microkernel import SovereignMicrokernel
from sarita_runtime.kernel.core_isolation.runtime_core_allocator import RuntimeCoreAllocator

async def run_extreme_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Extreme Physical Validation (Phase 69)...")

    # 1. Core Isolation Validation
    allocator = RuntimeCoreAllocator()
    nohz = allocator.validate_nohz_full()
    logging.info(f"Validation: Kernel NO_HZ_FULL: {nohz}")

    success = allocator.allocate_exclusive_cores("0-1")
    logging.info(f"Validation: Core Isolation Attempt: {success}")

    # 2. Nervous System Registration
    mk = SovereignMicrokernel()
    await mk.boot()

    task_id = "EXT-999"
    mk.unified_authority.execution_graph.register_material_execution(task_id, {"type": "EXTREME_WORKLOAD"})
    logging.info("Validation: Workload registered in Runtime Nervous System.")

    # 3. Memory Sovereignty (Hugepages)
    from sarita_runtime.kernel.memory_fabric.hugepage_authority import HugepageAuthority
    huge = HugepageAuthority(node_id=0)
    logging.info(f"Validation: Free hugepages before: {huge.get_free_hugepages()}")

    logging.info("Extreme Physical Validation COMPLETE.")

if __name__ == "__main__":
    asyncio.run(run_extreme_validation())
