import logging
import os

class PhysicalInterruptRouter:
    """
    Sovereign interrupt routing.
    Material enforcement via /proc/irq/smp_affinity.
    """
    def __init__(self):
        self.irq_base = "/proc/irq"

    def route_irq_to_core(self, irq_id: int, cpu_id: int):
        logging.info(f"IRQ Router: Materializing affinity for IRQ {irq_id} to Core {cpu_id}")
        mask = 1 << cpu_id
        path = os.path.join(self.irq_base, str(irq_id), "smp_affinity")

        if not os.path.exists(path):
            logging.warning(f"IRQ Router: IRQ {irq_id} path not found. Skipping material enforcement.")
            return False

        try:
            with open(path, "w") as f:
                f.write(f"{mask:x}")
            return True
        except PermissionError:
            logging.error(f"IRQ Router: Root required for material IRQ routing.")
        except Exception as e:
            logging.error(f"IRQ Router: Affinity enforcement failed: {e}")
        return False
