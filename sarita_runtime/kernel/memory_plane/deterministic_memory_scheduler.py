import logging
import os

class DeterministicMemoryScheduler:
    """
    Governs memory pressure and deterministic memory limits via cgroups v2.
    """
    def __init__(self, cgroup_base="/sys/fs/cgroup/sarita_governance"):
        self.cgroup_base = cgroup_base

    async def set_memory_limit(self, pid: int, max_bytes: int, high_bytes: int = None):
        logging.info(f"Memory Scheduler: Setting memory limit for PID {pid} to {max_bytes} bytes")
        try:
            pid_cgroup = os.path.join(self.cgroup_base, f"proc_{pid}")
            os.makedirs(pid_cgroup, exist_ok=True)

            with open(os.path.join(pid_cgroup, "memory.max"), "w") as f:
                f.write(str(max_bytes))

            if high_bytes:
                with open(os.path.join(pid_cgroup, "memory.high"), "w") as f:
                    f.write(str(high_bytes))

            # Ensure process is in this cgroup
            with open(os.path.join(pid_cgroup, "cgroup.procs"), "w") as f:
                f.write(str(pid))
            return True
        except Exception as e:
            logging.error(f"Memory Scheduler: Failed to set memory limits for PID {pid}: {e}")
            return False

    async def get_current_usage(self, pid: int):
        path = os.path.join(self.cgroup_base, f"proc_{pid}", "memory.current")
        if os.path.exists(path):
            with open(path, "r") as f:
                return int(f.read().strip())
        return 0

    async def reclaim_memory(self, pid: int, bytes_to_reclaim: int):
        logging.info(f"Memory Scheduler: Reclaiming {bytes_to_reclaim} bytes from PID {pid}")
        path = os.path.join(self.cgroup_base, f"proc_{pid}", "memory.reclaim")
        if os.path.exists(path):
            try:
                with open(path, "w") as f:
                    f.write(str(bytes_to_reclaim))
                return True
            except Exception as e:
                logging.error(f"Memory Scheduler: Reclaim failed: {e}")
        return False
