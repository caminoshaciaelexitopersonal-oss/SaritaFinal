import asyncio
import logging
import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.microkernel_fabric.sovereign_microkernel import SovereignMicrokernel

async def run_host_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Sovereign Physical Host Validation...")

    mk = SovereignMicrokernel()
    await mk.boot()

    # 1. Frequency Validation
    success = await mk.frequency_authority.lock_cpu_frequency(0, 3000000)
    logging.info(f"Validation: CPU Frequency Lock Success: {success}")

    # 2. Thermal Validation
    temp = await mk.thermal_authority.audit_thermal_pressure()
    logging.info(f"Validation: CPU Temperature: {temp}C")

    logging.info("Sovereign Physical Host Validation COMPLETE.")

if __name__ == "__main__":
    asyncio.run(run_host_validation())
