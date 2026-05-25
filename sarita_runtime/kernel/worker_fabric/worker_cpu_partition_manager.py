import logging
import os

class WorkerCpuPartitionManager:
    """
    Manages physical CPU partitions for persistent workers.
    """
    def __init__(self, cgroup_base="/sys/fs/cgroup/sarita_governance"):
        self.cgroup_base = cgroup_base

    def allocate_partition(self, partition_id: str, cpu_list: str):
        logging.info(f"Worker Partition: Allocating CPUs {cpu_list} for {partition_id}")
        path = os.path.join(self.cgroup_base, "worker_pool", partition_id)
        try:
            os.makedirs(path, exist_ok=True)
            with open(os.path.join(path, "cpuset.cpus"), "w") as f:
                f.write(cpu_list)
            with open(os.path.join(path, "cpuset.mems"), "w") as f:
                f.write("0")
            return True
        except Exception as e:
            logging.error(f"Worker Partition: Allocation failure: {e}")
            return False
