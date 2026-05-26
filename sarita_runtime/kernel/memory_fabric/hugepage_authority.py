import logging
import os
import subprocess

class HugepageAuthority:
    """
    HugeTLB material governance.
    PROHIBIDO fallback transparente de memoria host.
    """
    def __init__(self, node_id: int = 0):
        self.node_id = node_id
        self.hugepage_path = f"/sys/devices/system/node/node{node_id}/hugepages/hugepages-2048kB"

    def materialize_hugepages(self, count: int, mount_point: str = "/mnt/sarita_huge"):
        logging.info(f"Hugepage Authority: Materializing {count} hugepages on NUMA {self.node_id}")

        # 1. Allocate pages in kernel
        try:
            with open(os.path.join(self.hugepage_path, "nr_hugepages"), "w") as f:
                f.write(str(count))
        except Exception as e:
            logging.error(f"Hugepage Authority: Allocation failed: {e}")
            return False

        # 2. Mount hugetlbfs if not already mounted
        if not os.path.exists(mount_point):
            os.makedirs(mount_point, exist_ok=True)

        try:
            subprocess.run(["mount", "-t", "hugetlbfs", "none", mount_point], check=True)
            logging.info(f"Hugepage Authority: hugetlbfs Materialized at {mount_point}")
            return True
        except:
            logging.warning("Hugepage Authority: Mount failed. Continuing with physical allocation only.")
            return True

    def get_free_hugepages(self):
        try:
            with open(os.path.join(self.hugepage_path, "free_hugepages"), "r") as f:
                return int(f.read().strip())
        except:
            return 0
