import logging
import os
import signal

class RuntimeFenceAuthority:
    """
    Materializes physical fencing.
    Capacidad REAL de congelar execution domains y aislar workers.
    """
    def __init__(self, cgroup_base="/sys/fs/cgroup/sarita_governance"):
        self.cgroup_base = cgroup_base

    def freeze_domain(self, domain_id: str):
        logging.critical(f"Fence Authority: FREEZING domain {domain_id}")
        path = os.path.join(self.cgroup_base, domain_id, "cgroup.freeze")
        if os.path.exists(path):
            try:
                with open(path, "w") as f:
                    f.write("1")
                return True
            except Exception as e:
                logging.error(f"Fence Authority: Freeze FAILED: {e}")
        return False

    def unfreeze_domain(self, domain_id: str):
        logging.info(f"Fence Authority: Unfreezing domain {domain_id}")
        path = os.path.join(self.cgroup_base, domain_id, "cgroup.freeze")
        if os.path.exists(path):
            with open(path, "w") as f:
                f.write("0")

    def revoke_execution_chain(self, pid: int):
        logging.critical(f"Fence Authority: REVOKING execution for PID {pid}")
        try:
            os.kill(pid, signal.SIGKILL)
            return True
        except:
            return False
