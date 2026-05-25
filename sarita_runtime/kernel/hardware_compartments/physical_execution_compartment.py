import logging
import os

class PhysicalExecutionCompartment:
    """
    Creates deterministic hardware execution compartments.
    Materialized via cgroup cpuset.cpus and cpuset.mems.
    """
    def __init__(self, compartment_id: str, cgroup_base="/sys/fs/cgroup/sarita_governance"):
        self.compartment_id = compartment_id
        self.path = os.path.join(cgroup_base, compartment_id)

    def initialize_compartment(self, cpus: str, mems: str = "0"):
        logging.info(f"Compartment: Materializing {self.compartment_id} on CPUs {cpus}")
        try:
            os.makedirs(self.path, exist_ok=True)
            with open(os.path.join(self.path, "cpuset.cpus"), "w") as f:
                f.write(cpus)
            with open(os.path.join(self.path, "cpuset.mems"), "w") as f:
                f.write(mems)
            return True
        except Exception as e:
            logging.error(f"Compartment: Failed to initialize physical isolation: {e}")
            return False

    def bind_process(self, pid: int):
        try:
            with open(os.path.join(self.path, "cgroup.procs"), "w") as f:
                f.write(str(pid))
            return True
        except Exception as e:
            logging.error(f"Compartment: Failed to bind PID {pid}: {e}")
            return False
