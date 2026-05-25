import logging
import os
import signal

class PhysicalEnforcementGateway:
    """
    Physical Enforcement Plane.
    Allows REAL enforcement: suspension, cgroup freezing, CPU set blocking.
    """
    def __init__(self, cgroup_base="/sys/fs/cgroup/sarita_governance"):
        self.cgroup_base = cgroup_base

    async def freeze_execution_domain(self, domain_id: str):
        logging.warning(f"Enforcement Gateway: FREEZING execution domain {domain_id}")
        path = os.path.join(self.cgroup_base, domain_id, "cgroup.freeze")
        if os.path.exists(path):
            try:
                with open(path, "w") as f:
                    f.write("1")
                return True
            except Exception as e:
                logging.error(f"Enforcement Gateway: Failed to freeze cgroup: {e}")
        return False

    async def suspend_process(self, pid: int):
        logging.warning(f"Enforcement Gateway: Suspending PID {pid}")
        try:
            os.kill(pid, signal.SIGSTOP)
            return True
        except Exception as e:
            logging.error(f"Enforcement Gateway: Failed to suspend PID {pid}: {e}")
        return False

    async def resume_process(self, pid: int):
        logging.info(f"Enforcement Gateway: Resuming PID {pid}")
        try:
            os.kill(pid, signal.SIGCONT)
            return True
        except Exception as e:
            logging.error(f"Enforcement Gateway: Failed to resume PID {pid}: {e}")
        return False
