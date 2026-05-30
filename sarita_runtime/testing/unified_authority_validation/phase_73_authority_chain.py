import logging
import sys
import os
import time

# Ensure we can import the kernel
sys.path.append(os.getcwd())

from sarita_runtime.kernel.runtime_cortex.sovereign_cortex import SovereignCortex
from sarita_runtime.kernel.runtime_ledger.sovereign_audit_ledger import SovereignAuditLedger
from sarita_runtime.kernel.constitutional_execution.constitutional_authority import ConstitutionalAuthority
from sarita_runtime.kernel.sovereign_enforcement_fabric import SovereignEnforcementFabric

def test_single_linear_authority_chain():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Starting SINGLE CHAIN AUTHORITY VALIDATION (Phase 73.9)")

    # 1. Initialize Evidence Ledger
    ledger = SovereignAuditLedger("validation_audit.db")

    # 2. Initialize Constitution
    constitution = ConstitutionalAuthority(ledger)

    # 3. Initialize Cortex (Cognition)
    cortex = SovereignCortex()
    cortex.boot_sovereign_cortex()

    # 4. Initialize Enforcement (Hardware)
    enforcement = SovereignEnforcementFabric(cortex.nervous_system)

    # --- EXECUTION FLOW ---

    # A. Telemetry Assimilation
    logging.info("STEP A: Assimilating Telemetry")
    cortex.process_telemetry_signal("THERMAL_SENSOR_0", "TEMPERATURE", 85.0)

    # B. Constitutional Authorization
    logging.info("STEP B: Validating Execution Legitimacy")
    task_request = {"id": "CRITICAL_SYSTEM_SYNC", "epoch": 1, "lineage": "KERNEL_INIT"}
    if not constitution.validate_execution_legitimacy(task_request):
        raise Exception("Constitutional validation failed!")

    # C. Task Dispatch (The Scheduler)
    logging.info("STEP C: Dispatching Task to Physical Scheduler")

    execution_evidence = []

    def material_task_logic():
        logging.info("EXECUTING MATERIAL TASK LOGIC")
        # D. Material Enforcement (IO)
        logging.info("STEP D: Executing Material IO via Enforcement Fabric")
        enforcement.execute_material_io("CRITICAL_SYSTEM_SYNC", "PHYSICAL_COMMIT", {"sector": 0})
        execution_evidence.append("TASK_COMPLETED")

    cortex.dispatch_sovereign_task("CRITICAL_SYSTEM_SYNC", material_task_logic, cpu_affinity=0)

    # Wait for physical thread to pick it up
    timeout = 5
    start_time = time.time()
    while not execution_evidence and time.time() - start_time < timeout:
        time.sleep(0.1)

    if not execution_evidence:
        raise Exception("Task execution timed out!")

    # E. Evidence Verification
    logging.info("STEP E: Verifying Evidence Chain")
    is_valid, msg = ledger.verify_integrity()
    logging.info(f"Integrity Check: {msg}")

    if not is_valid:
        raise Exception(f"Ledger integrity failed: {msg}")

    logging.info("PHASE 73.9 SINGLE CHAIN VALIDATION: SUCCESSFUL")

if __name__ == "__main__":
    try:
        test_single_linear_authority_chain()
    except Exception as e:
        logging.error(f"VALIDATION FAILED: {e}")
        sys.exit(1)
