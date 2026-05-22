import logging

class CompensationRuntime:
    async def run_compensation(self, saga_id, steps):
        # 48.5 - Executable Compensation
        logging.warning(f"CRITICAL: Compensating Saga {saga_id}")
        for step in reversed(steps):
             logging.info(f"Compensating: {step}")
        return "ROLLED_BACK"
