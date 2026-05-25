import logging
import os

class DmaTopologyValidator:
    """
    Detects DMA pressure and NUMA interaction.
    Materialized for PCI device locality.
    """
    def __init__(self):
        self.pci_path = "/sys/bus/pci/devices"

    async def get_device_numa_node(self, device_id: str):
        """
        Reads the local NUMA node for a physical PCI device.
        """
        path = os.path.join(self.pci_path, device_id, "numa_node")
        if os.path.exists(path):
            with open(path, "r") as f:
                node = int(f.read().strip())
                # -1 means no specific node
                return node if node != -1 else 0
        return 0

    async def validate_dma_locality(self, device_id: str, target_node: int):
        node = await self.get_device_numa_node(device_id)
        logging.info(f"DMA Validator: Device {device_id} is on NUMA {node}. Expected {target_node}")
        return node == target_node
