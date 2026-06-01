import logging
import threading
from typing import Dict, Any, List
from sarita_runtime.kernel.runtime_graph.physical_execution_vertex import PhysicalExecutionVertex

class UnifiedExecutionGraph:
    """
    Unified Execution Graph (Phase 73).
    The SINGLE system nervous system. All decisions originate here.
    REFACTORED PHASE 74: Fixed lock initialization and lineage support.
    """
    def __init__(self):
        self._lock = threading.Lock() # Initialized lock
        self.vertices = []
        # Material physical state
        self.ownership = {}
        self.global_pressure = 0.0
        self.active_epoch = 0
        self.material_runqueue = [] # Consolidated runqueue
        self.completed_tasks = set()

    def add_authorized_task(self, task: Dict[str, Any]):
        with self._lock:
            self.material_runqueue.append(task)

    def get_next_authorized_task(self):
        with self._lock:
            if self.material_runqueue:
                return self.material_runqueue.pop(0)
        return None

    def mark_execution_complete(self, task_id: str):
        with self._lock:
            self.completed_tasks.add(task_id)

    def register_material_decision(self, task_id: str, action: str, evidence: dict):
        logging.info(f"Sovereign Bus: Committing DECISION {action} for {task_id}")
        # Register in graph for causal auditing
        vertex = self.register_material_vertex(task_id, {"action": action, "evidence": evidence})
        return vertex

    def register_material_vertex(self, task_id: str, payload: Dict[str, Any]):
        vertex = PhysicalExecutionVertex(task_id, payload)
        with self._lock:
            self.vertices.append(vertex)
        return vertex

    def calculate_saturation(self, subsystem_signals: dict):
        # Centralized pressure calculation
        score = sum(subsystem_signals.values()) / len(subsystem_signals) if subsystem_signals else 0.0
        self.global_pressure = score
        return score

    def update_ownership(self, resource: str, owner_id: str):
        with self._lock:
            self.ownership[resource] = owner_id

    def get_vertex(self, task_id: str):
        with self._lock:
            for v in reversed(self.vertices):
                if v.task_id == task_id:
                    return v
        return None

    def get_all_vertices(self):
        with self._lock:
            return list(self.vertices)
