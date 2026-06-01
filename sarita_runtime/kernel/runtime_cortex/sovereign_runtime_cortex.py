import logging
import os
import threading
from typing import Dict, Any
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.scheduling_fabric.sovereign_scheduler import SovereignScheduler

class SovereignRuntimeCortex:
    """
    Unified Sovereign Physical Cortex (Phase 70).
    Centralizes all hardware decisions and correlates physical signals.
    REFACTORED PHASE 74: Validated as the single entry point to the Nervous System.
    """
    def __init__(self):
        self.nervous_system = UnifiedExecutionGraph()
        # Corrected class name for Phase 74 convergence
        self.scheduler = SovereignScheduler(self.nervous_system)
        self.is_active = False

    def boot_sovereign_cortex(self):
        logging.info("Cortex: Materializing Unified Physical Cortex.")
        # Physical substrate initialization
        self.scheduler.start_physical_dispatch()
        self.is_active = True
        return True

    def assimilate_physical_signal(self, subsystem: str, signal: str, value: float):
        logging.info(f"Cortex: Assimilating {signal} from {subsystem} ({value})")
        # Direct correlation in the Nervous System (UnifiedExecutionGraph)
        if signal == "TEMPERATURE" or signal == "PRESSURE":
            self.nervous_system.calculate_saturation({subsystem: value})
        elif signal == "SCHEDULER_JITTER":
            # Direct pressure update to the graph
            self.nervous_system.calculate_saturation({"scheduler": value})
