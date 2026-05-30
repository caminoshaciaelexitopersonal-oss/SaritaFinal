import logging
import os
from typing import List

class SovereignCPUScheduler:
    """
    Sovereign CPU Scheduling Fabric.
    Governs CPU allocation and affinity using cgroups v2 and sched_setaffinity.
    """
    def __init__(self):
        self.cgroup_base = "/sys/fs/cgroup/sarita_governance"
        self._ensure_cgroup_structure()

    def _ensure_cgroup_structure(self):
        try:
            if not os.path.exists(self.cgroup_base):
                # In production this requires root
                os.makedirs(self.cgroup_base, exist_ok=True)
                with open(os.path.join(self.cgroup_base, "cgroup.subtree_control"), "w") as f:
                    f.write("+cpu +cpuset +memory +io")
            logging.info(f"Sovereign Scheduler: Cgroup base {self.cgroup_base} initialized.")
        except Exception as e:
            logging.warning(f"Sovereign Scheduler: Failed to initialize cgroups: {e}. Running in degraded mode.")

    async def assign_cpu_affinity(self, pid: int, cpus: List[int]):
        logging.info(f"Sovereign Scheduler: Assigning PID {pid} to CPUs {cpus}")
        try:
            os.sched_setaffinity(pid, cpus)

            # Also enforce via cpuset cgroup if possible
            pid_cgroup = os.path.join(self.cgroup_base, f"proc_{pid}")
            os.makedirs(pid_cgroup, exist_ok=True)
            cpus_str = ",".join(map(str, cpus))
            with open(os.path.join(pid_cgroup, "cpuset.cpus"), "w") as f:
                f.write(cpus_str)
            with open(os.path.join(pid_cgroup, "cgroup.procs"), "w") as f:
                f.write(str(pid))

            return True
        except Exception as e:
            logging.error(f"Sovereign Scheduler: Failed to set affinity for PID {pid}: {e}")
            return False

    def get_psi_metrics(self):
        try:
            metrics = {}
            for resource in ["cpu", "memory", "io"]:
                path = f"/proc/pressure/{resource}"
                if os.path.exists(path):
                    with open(path, "r") as f:
                        metrics[resource] = f.read().strip()
            return metrics
        except Exception as e:
            return f"PSI metrics retrieval failed: {e}"
