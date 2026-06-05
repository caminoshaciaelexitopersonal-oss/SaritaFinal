import logging
import os
import threading
import time
from typing import List, Dict, Any
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.hardware_authority.physical_resource_authority import PhysicalResourceAuthority

class SovereignScheduler:
    """
    Consolidated Sovereign Scheduler (Phase 73).
    REFACTORED PHASE 74: Delegating CPU affinity to PhysicalResourceAuthority.
    """
    def __init__(self, nervous_system: UnifiedExecutionGraph):
        self.nervous_system = nervous_system
        self.hardware_authority = PhysicalResourceAuthority(nervous_system)
        self.cgroup_base = "/sys/fs/cgroup/sarita_governance"
        self._ensure_cgroup_structure()
        self.dispatch_thread = None
        self.is_running = False

    def _ensure_cgroup_structure(self):
        try:
            if not os.path.exists(self.cgroup_base):
                os.makedirs(self.cgroup_base, exist_ok=True)
        except Exception as e:
            logging.error(f"Scheduler: Cgroup creation failed: {e}")

    def start_physical_dispatch(self):
        """Starts the physical dispatch loop in a dedicated thread."""
        if self.is_running:
            return
        self.is_running = True
        self.dispatch_thread = threading.Thread(target=self._dispatch_loop, name="SchedulerDispatch", daemon=True)
        self.dispatch_thread.start()
        logging.info("Sovereign Scheduler: Physical dispatch loop started.")

    def shutdown(self):
        """Cleanly stops the dispatcher."""
        self.is_running = False
        if self.dispatch_thread:
            self.dispatch_thread.join(timeout=5)
        logging.info("Sovereign Scheduler: Operational shutdown complete.")

    def _dispatch_loop(self):
        while self.is_running:
            task = self.nervous_system.get_next_authorized_task()
            if task:
                self._execute_material_task(task)
            else:
                time.sleep(0.001)

    def _execute_material_task(self, task):
        logging.info(f"Sovereign Scheduler: Dispatching Task {task['id']}")
        if 'cpu_affinity' in task:
            self.hardware_authority.enforce_cpu_affinity(0, [task['cpu_affinity']])

        try:
            task['logic']()
            self.nervous_system.mark_execution_complete(task['id'])
        except Exception as e:
            logging.error(f"Sovereign Scheduler: Task {task['id']} failed: {e}")

    def assign_cpu_affinity(self, pid: int, cpus: List[int]):
        return self.hardware_authority.enforce_cpu_affinity(pid, cpus)

    def get_psi_metrics(self):
        metrics = {}
        try:
            for resource in ["cpu", "memory", "io"]:
                path = f"/proc/pressure/{resource}"
                if os.path.exists(path):
                    with open(path, "r") as f:
                        metrics[resource] = f.read().strip()
        except Exception as e:
            logging.error(f"Scheduler: PSI access failed: {e}")
        return metrics
