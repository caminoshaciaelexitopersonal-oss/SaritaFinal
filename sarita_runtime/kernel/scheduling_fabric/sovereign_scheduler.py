import logging
import os
import threading
import time
from typing import List, Dict, Any
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class SovereignScheduler:
    """
    Consolidated Sovereign Scheduler (Phase 73).
    Governs CPU allocation, affinity, and deterministic task dispatch.
    """
    def __init__(self, nervous_system: UnifiedExecutionGraph):
        self.nervous_system = nervous_system
        self.cgroup_base = "/sys/fs/cgroup/sarita_governance"
        self._ensure_cgroup_structure()
        self.dispatch_thread = None
        self.is_running = False

    def _ensure_cgroup_structure(self):
        try:
            if not os.path.exists(self.cgroup_base):
                os.makedirs(self.cgroup_base, exist_ok=True)
                # Note: Requires root/CAP_SYS_RESOURCE
        except Exception:
            pass

    def start_physical_dispatch(self):
        """Starts the physical dispatch loop in a dedicated thread."""
        if self.is_running:
            return
        self.is_running = True
        self.dispatch_thread = threading.Thread(target=self._dispatch_loop, daemon=True)
        self.dispatch_thread.start()
        logging.info("Sovereign Scheduler: Physical dispatch loop started.")

    def _dispatch_loop(self):
        while self.is_running:
            # Material task selection from the nervous system
            task = self.nervous_system.get_next_authorized_task()
            if task:
                self._execute_material_task(task)
            else:
                time.sleep(0.001) # 1ms precision for the idle loop

    def _execute_material_task(self, task):
        logging.info(f"Sovereign Scheduler: Dispatching Task {task['id']} to CPU {task.get('cpu_affinity')}")
        # 1. Enforce affinity
        if 'cpu_affinity' in task:
            try:
                os.sched_setaffinity(0, [task['cpu_affinity']])
            except Exception:
                pass

        # 2. Execute task logic (material call)
        try:
            task['logic']()
            self.nervous_system.mark_execution_complete(task['id'])
        except Exception as e:
            logging.error(f"Sovereign Scheduler: Task {task['id']} failed: {e}")

    def assign_cpu_affinity(self, pid: int, cpus: List[int]):
        logging.info(f"Sovereign Scheduler: Assigning PID {pid} to CPUs {cpus}")
        try:
            os.sched_setaffinity(pid, cpus)
            return True
        except Exception:
            return False

    def get_psi_metrics(self):
        metrics = {}
        try:
            for resource in ["cpu", "memory", "io"]:
                path = f"/proc/pressure/{resource}"
                if os.path.exists(path):
                    with open(path, "r") as f:
                        metrics[resource] = f.read().strip()
        except Exception:
            pass
        return metrics
