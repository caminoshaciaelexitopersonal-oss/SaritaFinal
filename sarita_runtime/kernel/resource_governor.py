import psutil
import logging

class ResourceGovernor:
    def __init__(self):
        self.memory_threshold = 85.0 # %
        self.cpu_threshold = 90.0 # %

    def check_system_pressure(self):
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        logging.info(f"System Load - CPU: {cpu}%, MEM: {mem}%")

        if cpu > self.cpu_threshold or mem > self.memory_threshold:
            return "CRITICAL_PRESSURE"
        return "STABLE"

    def apply_adaptive_scaling(self, domain, pressure_score):
        if pressure_score == "CRITICAL_PRESSURE":
            logging.critical(f"Applying adaptive throttling to domain: {domain}")
            return "THROTTLED"
        return "NORMAL"

if __name__ == "__main__":
    rg = ResourceGovernor()
    print(rg.check_system_pressure())
