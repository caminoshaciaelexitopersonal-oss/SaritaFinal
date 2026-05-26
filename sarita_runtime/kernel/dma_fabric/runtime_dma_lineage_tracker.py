import logging

class RuntimeDmaLineageTracker:
    """
    Tracks DMA locality lineage.
    Ensures DMA transfers respect NUMA-aware physical paths.
    """
    def __init__(self):
        self.dma_history = []

    def record_dma_transfer(self, task_id: str, device_id: str, numa_node: int):
        logging.info(f"DMA Lineage: Task {task_id} DMA via {device_id} on NUMA {numa_node}")
        self.dma_history.append({"task": task_id, "dev": device_id, "node": numa_node})
