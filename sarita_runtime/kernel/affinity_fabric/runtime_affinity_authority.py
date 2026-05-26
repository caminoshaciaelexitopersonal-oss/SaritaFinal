import logging

class RuntimeAffinityAuthority:
    """
    Centralizes physical ownership of CPUs, NUMA nodes, and IRQs.
    Provides a single affinity graph for the runtime.
    """
    def __init__(self):
        self.cpu_owners = {}
        self.irq_owners = {}

    def assign_cpu(self, cpu_id: int, owner_id: str):
        logging.info(f"Affinity Authority: CPU {cpu_id} CLAIMED by {owner_id}")
        self.cpu_owners[cpu_id] = owner_id

    def assign_irq(self, irq_id: int, owner_id: str, cpu_mask: str):
        logging.info(f"Affinity Authority: IRQ {irq_id} CLAIMED by {owner_id}")
        self.irq_owners[irq_id] = owner_id
        return True

    def validate_ownership(self, resource_id: str, requester_id: str):
        if resource_id.startswith("CPU"):
            cid = int(resource_id.split("-")[1])
            return self.cpu_owners.get(cid) == requester_id
        return False
