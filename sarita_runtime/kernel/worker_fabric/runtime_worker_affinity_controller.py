import logging
import os

class RuntimeWorkerAffinityController:
    """
    Ensures persistent workers maintain their hardware pinning.
    Prevents affinity drift.
    """
    def __init__(self):
        pass

    def validate_worker_pinning(self, pid: int, expected_cpus: set):
        try:
            current_affinity = os.sched_getaffinity(pid)
            if current_affinity != expected_cpus:
                logging.warning(f"Affinity Drift: PID {pid} moved to {current_affinity}. Re-pinning to {expected_cpus}")
                os.sched_setaffinity(pid, expected_cpus)
                return False
            return True
        except:
            return False
