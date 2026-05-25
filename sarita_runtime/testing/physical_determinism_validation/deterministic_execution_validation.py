import asyncio
import logging
import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.runtime_determinism.deterministic_latency_controller import DeterministicLatencyController
from sarita_runtime.kernel.runtime_truth.runtime_latency_constitution import RuntimeLatencyConstitution
from sarita_runtime.kernel.scheduling_fabric.rt_preemption_validator import RtPreemptionValidator

async def run_determinism_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Physical Deterministic Runtime Validation...")

    # 1. RT Kernel Check
    rt_val = RtPreemptionValidator()
    is_rt = rt_val.is_rt_kernel()
    logging.info(f"Validation: PREEMPT_RT Active: {is_rt}")

    # 2. Latency and Jitter Validation
    latency_ctrl = DeterministicLatencyController()
    constitution = RuntimeLatencyConstitution()

    async def dummy_task():
        await asyncio.sleep(0.001)

    logging.info("Validation: Measuring deterministic task latency...")
    for _ in range(10):
        await latency_ctrl.measure_execution_latency(dummy_task)

    avg_lat = sum(latency_ctrl.latency_stats) / len(latency_ctrl.latency_stats)
    is_legit = await constitution.validate_timing_legitimacy("NORMAL", avg_lat)

    if is_legit:
        logging.info(f"Validation: Determinism within budget ({avg_lat:.4f}ms). SUCCESS.")
    else:
        logging.error(f"Validation: Determinism budget violation! ({avg_lat:.4f}ms). FAILED.")

    logging.info("Physical Deterministic Runtime Validation COMPLETE.")

if __name__ == "__main__":
    asyncio.run(run_determinism_validation())
