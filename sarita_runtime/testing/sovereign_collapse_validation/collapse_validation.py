import asyncio
import logging
import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.microkernel_fabric.sovereign_microkernel import SovereignMicrokernel
from sarita_runtime.kernel.runtime_state_machine.execution_state_controller import ExecutionState

async def run_collapse_validation():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Sovereign Runtime Collapse Validation (Phase 67)...")

    mk = SovereignMicrokernel()
    await mk.boot()

    # 1. State machine validation
    if mk.state_machine.current_state == ExecutionState.VERIFIED:
        logging.info("Validation: State Machine Transition SUCCESS.")
    else:
        logging.error(f"Validation: State Machine in unexpected state: {mk.state_machine.current_state}")

    # 2. Unified Authority Task Submission
    op = {"id": "COL-001", "type": "UNIFIED_EXECUTION", "provenance_token": "UNIFIED-KEY"}
    success = await mk.submit_task("COL-001", op)

    if success:
        logging.info("Validation: Unified Authority Dispatch SUCCESS.")
    else:
        logging.error("Validation: Unified Authority Dispatch FAILED.")

    # 3. Capability Audit
    from sarita_runtime.kernel.capability_plane.runtime_capability_validator import RuntimeCapabilityValidator
    cap_val = RuntimeCapabilityValidator()
    logging.info(f"Validation: Effective Capabilities: {cap_val.get_effective_capabilities()}")

    logging.info("Sovereign Runtime Collapse Validation COMPLETE.")

if __name__ == "__main__":
    asyncio.run(run_collapse_validation())
