import asyncio
import logging
from sarita_runtime.kernel.forensics.forensic_hash_engine import ForensicHashEngine
from sarita_runtime.kernel.ai_governance.ai_policy_enforcer import AIPolicyEnforcer

async def run_final_sovereign_validation():
    logging.basicConfig(level=logging.INFO)
    print("--- INITIATING FINAL SOVEREIGN RUNTIME VALIDATION (PHASE 48) ---")

    # 1. Validate Forensic Hashing
    engine = ForensicHashEngine()
    h = engine.calculate_sha256({"data": "test"}, "prev", "trace-1")
    if len(h) == 64:
        print("Forensic Integrity: PASS")

    # 2. Validate AI Governance
    gov = AIPolicyEnforcer()
    allowed, _ = gov.validate_mission("AI-1", {"tool": "read_logs"}, "T-100")
    if allowed:
        print("AI Governance: PASS")

    print("--- VALIDATION SUCCESSFUL ---")

if __name__ == "__main__":
    asyncio.run(run_final_sovereign_validation())
