import logging

class ExclusiveCpuDomains:
    """
    Manages ownership of exclusive CPU domains.
    PROHIBIDO sharing sovereign cores with non-constitutional tasks.
    """
    def __init__(self):
        self.domains = {}

    def register_exclusive_domain(self, domain_id: str, cpus: list):
        logging.info(f"CPU Domains: Registering exclusive domain {domain_id} for CPUs {cpus}")
        self.domains[domain_id] = cpus

    def is_cpu_reserved(self, cpu_id: int):
        for cpus in self.domains.values():
            if cpu_id in cpus: return True
        return False
