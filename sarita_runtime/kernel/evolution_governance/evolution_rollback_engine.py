import time

class EvolutionRollbackEngine:
    """
    Enables total or partial reversal of evolutionary changes.
    """
    def __init__(self, recovery_framework, reversal_validator, restoration_engine, ledger):
        self.recovery_framework = recovery_framework
        self.reversal_validator = reversal_validator
        self.restoration_engine = restoration_engine
        self.ledger = ledger

    def execute_rollback(self, evolution_id, scope="total"):
        print(f"[EvolutionRollbackEngine] Initiating {scope} rollback for {evolution_id}...")

        can_reverse = self.reversal_validator.validate_reversal(evolution_id)
        if not can_reverse:
            return {"status": "FAILED", "reason": "UNSAFE_REVERSAL"}

        recovery_plan = self.recovery_framework.plan_recovery(evolution_id, scope)
        result = self.restoration_engine.restore_constitution(recovery_plan)

        final_res = {
            "evolution_id": evolution_id,
            "scope": scope,
            "status": "SUCCESS",
            "timestamp": time.time()
        }

        self.ledger.record(final_res)
        return final_res
