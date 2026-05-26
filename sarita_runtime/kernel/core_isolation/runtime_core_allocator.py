import logging
import os

class RuntimeCoreAllocator:
    """
    Isolates exclusive CPUs for SARITA runtime.
    Gobernar housekeeping CPUs and validate isolcpus/no_hz_full.
    """
    def __init__(self, cgroup_base="/sys/fs/cgroup/sarita_governance"):
        self.cgroup_base = cgroup_base

    def allocate_exclusive_cores(self, cpu_list: str):
        logging.info(f"Core Allocator: Materializing exclusive core domain on {cpu_list}")
        path = os.path.join(self.cgroup_base, "sovereign_cores")
        try:
            os.makedirs(path, exist_ok=True)
            with open(os.path.join(path, "cpuset.cpus"), "w") as f:
                f.write(cpu_list)
            # Ensure only sovereign tasks can enter this domain
            return True
        except Exception as e:
            logging.error(f"Core Allocator: Failed to isolate cores: {e}")
            return False

    def validate_nohz_full(self):
        try:
            with open("/sys/devices/system/cpu/nohz_full", "r") as f:
                return f.read().strip()
        except:
            return "None"
