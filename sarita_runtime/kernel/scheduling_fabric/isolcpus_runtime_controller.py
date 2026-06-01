import logging
import os

class IsolcpusRuntimeController:
    """
    Physical CPU isolation controller.
    Interfaces with kernel boot parameters (informational) and cgroups cpuset.
    """
    def __init__(self, cgroup_base="/sys/fs/cgroup/sarita_governance"):
        self.cgroup_base = cgroup_base

    def get_isolated_cpus_kernel(self):
        """Reads isolated CPUs from kernel command line."""
        try:
            with open("/proc/cmdline", "r") as f:
                cmdline = f.read()
                for part in cmdline.split():
                    if part.startswith("isolcpus="):
                        return part.split("=")[1]
        except:
            pass
        return "None"

    async def enforce_physical_isolation(self, cpu_group_name: str, cpus: str):
        """Creates a dedicated cpuset for isolated execution."""
        logging.info(f"Isolcpus Controller: Enforcing physical isolation on CPUs {cpus} for {cpu_group_name}")
        path = os.path.join(self.cgroup_base, cpu_group_name)
        try:
            os.makedirs(path, exist_ok=True)
            with open(os.path.join(path, "cpuset.cpus"), "w") as f:
                f.write(cpus)
            with open(os.path.join(path, "cpuset.mems"), "w") as f:
                f.write("0") # Default to node 0, will be refined by NUMA allocator
            return True
        except Exception as e:
            logging.error(f"Isolcpus Controller: Failed to enforce isolation: {e}")
            return False
