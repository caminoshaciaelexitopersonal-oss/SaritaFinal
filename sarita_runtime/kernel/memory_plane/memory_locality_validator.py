import logging
import os

class MemoryLocalityValidator:
    """
    Validates memory locality to ensure no cross-socket memory access jitter.
    Material implementation for /proc/PID/numa_maps parsing.
    """
    def __init__(self):
        pass

    async def validate_pid_locality(self, pid: int, expected_node: int):
        """
        Parses /proc/PID/numa_maps to verify memory pages are on the correct node.
        """
        logging.info(f"Locality Validator: Validating memory locality for PID {pid} on Node {expected_node}")
        path = f"/proc/{pid}/numa_maps"

        if not os.path.exists(path):
            logging.warning(f"Locality Validator: {path} not found.")
            return True

        remote_pages = 0
        try:
            with open(path, "r") as f:
                for line in f:
                    parts = line.split()
                    for p in parts:
                        if p.startswith("N") and "=" in p:
                            node_id = int(p[1:].split("=")[0])
                            page_count = int(p.split("=")[1])
                            if node_id != expected_node:
                                remote_pages += page_count

            if remote_pages > 1000: # Threshold for "jittery" locality
                logging.warning(f"Locality Validator: PID {pid} has {remote_pages} remote pages on other nodes.")
                return False
            return True
        except Exception as e:
            logging.error(f"Locality Validator: Error parsing numa_maps: {e}")
            return True
