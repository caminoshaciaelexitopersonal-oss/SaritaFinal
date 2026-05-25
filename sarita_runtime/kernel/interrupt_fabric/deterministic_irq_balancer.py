import logging
import os

class DeterministicIrqBalancer:
    """
    Balances interrupts deterministically to avoid jitter on isolated CPUs.
    Material implementation for moving IRQs away from protected CPU sets.
    """
    def __init__(self):
        self.irq_base = "/proc/irq"

    async def rebalance_irqs_sovereign(self, protected_cpus: list):
        """
        Moves all movable IRQs away from protected CPUs by updating smp_affinity.
        """
        logging.info(f"IRQ Balancer: Moving interrupts away from CPUs {protected_cpus}")

        # Calculate new affinity mask (all CPUs except protected ones)
        # Assuming 64-bit mask for simplicity
        mask = 0xFFFFFFFFFFFFFFFF
        for cpu in protected_cpus:
            mask &= ~(1 << cpu)

        # Format as comma-separated 32-bit hex words for Linux smp_affinity
        low = mask & 0xFFFFFFFF
        high = (mask >> 32) & 0xFFFFFFFF
        mask_hex = f"{high:08x},{low:08x}"

        try:
            if not os.path.exists(self.irq_base):
                logging.warning("IRQ Balancer: /proc/irq not found. Skipping physical rebalance.")
                return False

            for irq_dir in os.listdir(self.irq_base):
                if irq_dir.isdigit():
                    affinity_file = os.path.join(self.irq_base, irq_dir, "smp_affinity")
                    if os.path.exists(affinity_file):
                        # Some IRQs cannot be moved (e.g. cascade, timer)
                        try:
                            with open(affinity_file, "w") as f:
                                f.write(mask_hex)
                            logging.debug(f"IRQ Balancer: Moved IRQ {irq_dir} to mask {mask_hex}")
                        except OSError:
                            logging.debug(f"IRQ Balancer: IRQ {irq_dir} is not movable.")
            return True
        except Exception as e:
            logging.error(f"IRQ Balancer: Failed to rebalance IRQs: {e}")
            return False
