import logging
from typing import Dict, Any

class RuntimeDecisionEngine:
    """
    Sovereign Decision Engine.
    Executes material actions based on real telemetry.
    """
    def __init__(self, cortex):
        self.cortex = cortex

    def execute_sovereign_rebalance(self, signals: Dict[str, Any]):
        logging.info("Decision Engine: Evaluating physical state for rebalance.")

        # PSI correlation
        cpu_some = signals.get("cpu_psi_some", 0.0)
        temp = signals.get("temperature", 40.0)

        if temp > 80.0 or cpu_some > 50.0:
            logging.critical("Decision Engine: MATERIAL ACTION - Triggering urgent task migration.")
            # Trigger physical migration via scheduler
            return "MIGRATE_TASKS"

        return "STABLE"
