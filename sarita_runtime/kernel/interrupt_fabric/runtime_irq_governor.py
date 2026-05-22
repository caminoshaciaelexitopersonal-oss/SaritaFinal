import logging
import os

class RuntimeIRQGovernor:
    """
    Sovereign Interrupt Governance Layer.
    Physical awareness and control of hardware interrupts.
    """
    def __init__(self):
        self.proc_interrupts = "/proc/interrupts"
        self.irq_base = "/proc/irq"

    async def get_interrupt_counts(self):
        """Reads /proc/interrupts and parses current distribution."""
        if not os.path.exists(self.proc_interrupts):
            return {}

        with open(self.proc_interrupts, "r") as f:
            lines = f.readlines()

        # Simple parser for IRQ counts
        counts = {}
        for line in lines[1:]: # Skip header
            parts = line.split()
            if not parts: continue
            irq_id = parts[0].strip(":")
            if irq_id.isdigit():
                counts[irq_id] = parts[1:] # Counts per CPU
        return counts

    async def isolate_cpu_from_interrupts(self, cpu_id: int):
        """
        Attempts to remove a CPU from all IRQ affinities to isolate it for deterministic execution.
        """
        logging.info(f"IRQ Governor: Isolating CPU {cpu_id} from general interrupts.")
        cpu_mask = ~(1 << cpu_id)
        mask_hex = hex(cpu_mask & 0xFFFFFFFF).replace("0x", "")

        try:
            for irq_dir in os.listdir(self.irq_base):
                if irq_dir.isdigit():
                    affinity_file = os.path.join(self.irq_base, irq_dir, "smp_affinity")
                    if os.path.exists(affinity_file):
                        with open(affinity_file, "w") as f:
                            f.write(mask_hex)
            return True
        except Exception as e:
            logging.error(f"IRQ Governor: Failed to isolate CPU {cpu_id}: {e}")
            return False

    async def set_irq_affinity(self, irq_id: int, cpu_mask_hex: str):
        logging.info(f"IRQ Governor: Setting IRQ {irq_id} affinity to {cpu_mask_hex}")
        path = os.path.join(self.irq_base, str(irq_id), "smp_affinity")
        try:
            with open(path, "w") as f:
                f.write(cpu_mask_hex)
            return True
        except Exception as e:
            logging.error(f"IRQ Governor: Failed to set IRQ {irq_id} affinity: {e}")
            return False
