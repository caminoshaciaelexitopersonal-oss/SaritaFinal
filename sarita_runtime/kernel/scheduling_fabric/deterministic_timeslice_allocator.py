import logging
import os

class DeterministicTimesliceAllocator:
    """
    Allocates CPU timeslices using cgroup v2 cpu.max.
    """
    def __init__(self, cgroup_base="/sys/fs/cgroup/sarita_governance"):
        self.cgroup_base = cgroup_base

    async def allocate_timeslice(self, pid: int, quota_us: int, period_us: int = 100000):
        logging.info(f"Timeslice Allocator: Allocating {quota_us}us per {period_us}us to PID {pid}")
        try:
            pid_cgroup = os.path.join(self.cgroup_base, f"proc_{pid}")
            os.makedirs(pid_cgroup, exist_ok=True)

            with open(os.path.join(pid_cgroup, "cpu.max"), "w") as f:
                f.write(f"{quota_us} {period_us}")

            # Ensure process is in this cgroup
            with open(os.path.join(pid_cgroup, "cgroup.procs"), "w") as f:
                f.write(str(pid))
            return True
        except Exception as e:
            logging.error(f"Timeslice Allocator: Failed to set CPU quota for PID {pid}: {e}")
            return False

    async def throttle_process(self, pid: int):
        logging.warning(f"Timeslice Allocator: Throttling PID {pid} to minimum.")
        return await self.allocate_timeslice(pid, 1000) # 1ms per 100ms
