import logging
from typing import Dict, Any, List

class PhysicalExecutionVertex:
    """
    Physical execution vertex in the Unified Execution Graph.
    Toda ejecución posee lineage causal y affinity física.
    """
    def __init__(self, task_id: str, payload: Dict[str, Any]):
        self.task_id = task_id
        self.payload = payload
        self.status = "INIT"
        self.epoch = payload.get("epoch", 0)
        self.cpu_affinity = payload.get("cpu_affinity", [])
        self.dependencies = []
        self.execution_start_ns = 0
        self.execution_end_ns = 0

    def add_dependency(self, parent_id: str):
        self.dependencies.append(parent_id)

    def mark_executing(self, start_ns: int):
        self.status = "EXECUTING"
        self.execution_start_ns = start_ns

    def mark_completed(self, end_ns: int):
        self.status = "COMPLETED"
        self.execution_end_ns = end_ns
