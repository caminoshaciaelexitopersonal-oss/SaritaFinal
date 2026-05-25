import asyncio
import logging
import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.fencing_fabric.runtime_fence_authority import RuntimeFenceAuthority
from sarita_runtime.kernel.affinity_fabric.runtime_affinity_authority import RuntimeAffinityAuthority

async def run_fencing_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Material Fencing Validation...")

    fence = RuntimeFenceAuthority()
    affinity = RuntimeAffinityAuthority()

    # 1. CPU Ownership Validation
    affinity.assign_cpu(0, "WORKER-ALPHA")
    logging.info(f"Validation: CPU 0 ownership: {affinity.cpu_owners.get(0)}")

    # 2. Cgroup Freezing Intent
    # In sandbox we check if the path construction is correct and material
    success = fence.freeze_domain("critical_domain")
    logging.info(f"Validation: Freeze execution domain: {success}")

    logging.info("Material Fencing Validation COMPLETE.")

if __name__ == "__main__":
    asyncio.run(run_fencing_validation())
