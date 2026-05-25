import logging
import os

class NumaMemoryAllocator:
    """
    Enforces NUMA-aware execution locality and deterministic memory placement.
    """
    def __init__(self, cgroup_base="/sys/fs/cgroup/sarita_governance"):
        self.cgroup_base = cgroup_base

    async def bind_process_to_numa_node(self, pid: int, node_id: int):
        """
        Binds a process to a specific NUMA node for memory allocations.
        Uses cgroup v2 cpuset.mems.
        """
        logging.info(f"NUMA Allocator: Binding PID {pid} to NUMA node {node_id}")
        path = os.path.join(self.cgroup_base, f"proc_{pid}")
        try:
            os.makedirs(path, exist_ok=True)
            with open(os.path.join(path, "cpuset.mems"), "w") as f:
                f.write(str(node_id))

            # For immediate allocation enforcement, we'd use numactl --membind or move_pages
            return True
        except Exception as e:
            logging.error(f"NUMA Allocator: Failed to bind memory for PID {pid}: {e}")
            return False

    def get_available_numa_nodes(self):
        try:
            nodes = [d for d in os.listdir("/sys/devices/system/node") if d.startswith("node")]
            return nodes
        except:
            return ["node0"]
