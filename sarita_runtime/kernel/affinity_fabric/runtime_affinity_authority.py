import logging
import os

class RuntimeAffinityAuthority:
    """
    Centralizes ownership of hardware resources (CPUs, IRQs, NUMA).
    """
    def __init__(self):
        self.cpu_owners = {}
        self.irq_owners = {}

    def assign_cpu(self, cpu_id: int, owner_id: str):
        logging.info(f"Affinity Authority: Assigning CPU {cpu_id} to {owner_id}")
        self.cpu_owners[cpu_id] = owner_id
        # Material enforcement via os.sched_setaffinity would be called by the owner

    def assign_irq(self, irq_id: int, owner_id: str, cpu_mask: str):
        logging.info(f"Affinity Authority: Assigning IRQ {irq_id} to {owner_id} (Mask: {cpu_mask})")
        self.irq_owners[irq_id] = owner_id
        # Material enforcement
        path = f"/proc/irq/{irq_id}/smp_affinity"
        if os.path.exists(path):
            try:
                with open(path, "w") as f:
                    f.write(cpu_mask)
                return True
            except Exception as e:
                logging.error(f"Affinity Authority: IRQ assignment FAILED: {e}")
        return False
