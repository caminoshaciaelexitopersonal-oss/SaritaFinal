import logging
import threading
from typing import Dict, Any, List
from sarita_runtime.kernel.runtime_graph.physical_execution_vertex import PhysicalExecutionVertex

class UnifiedExecutionGraph:
    """
    Unified Execution Graph (Phase 73/74/75).
    The SINGLE system nervous system. All decisions originate here.
    FIXED PHASE 75: Separated material runqueue from persistent causal vertices.
    """
    def __init__(self):
        self._lock = threading.Lock()
        self.vertices = [] # Persistent append-only log of PhysicalExecutionVertex
        # Material physical state
        self.ownership = {}
        self.global_pressure = 0.0
        self.active_epoch = 0
        self.material_runqueue = [] # Consolidated volatile runqueue for scheduling
        self.completed_tasks = set()

    def add_authorized_task(self, task: Dict[str, Any]):
        """Adds a task to the material runqueue for the scheduler."""
        with self._lock:
            # Also register a vertex for the authorization event
            self.register_material_vertex(task.get('id', 'unknown'), {"action": "TASK_AUTHORIZED", "task": task})
            self.material_runqueue.append(task)

    def get_next_authorized_task(self):
        """Scheduler retrieval point. Consumes from runqueue but NOT from vertices."""
        with self._lock:
            if self.material_runqueue:
                return self.material_runqueue.pop(0)
        return None

    def mark_execution_complete(self, task_id: str):
        with self._lock:
            self.completed_tasks.add(task_id)
            self.register_material_vertex(task_id, {"action": "EXECUTION_COMPLETE"})

    def register_material_decision(self, task_id: str, action: str, evidence: dict):
        logging.info(f"Sovereign Bus: Committing DECISION {action} for {task_id}")
        # Register in graph for causal auditing
        vertex = self.register_material_vertex(task_id, {"action": action, "evidence": evidence})
        return vertex

    def register_material_vertex(self, task_id: str, payload: Dict[str, Any]):
        """The absolute authority for causal lineage."""
        vertex = PhysicalExecutionVertex(task_id, payload)
        # Ensure lock is held if called from outside, but here we expect caller or we lock
        # Check if already locked by current thread is complex, so we assume sub-calls from locked methods or we lock.
        # To be safe and simple, let's just ensure we only call this from within locked methods or lock it here.

        # Checking if we are already in a 'with self._lock' is not trivial in Python.
        # But our own methods above hold the lock.
        # Let's make this internal-ish or always lock.
        self._internal_register_vertex(vertex)
        return vertex

    def _internal_register_vertex(self, vertex):
        # This one doesn't lock, assuming caller does.
        # Actually, let's just make register_material_vertex lock and call this.
        with self._lock:
            self.vertices.append(vertex)

    def register_material_vertex(self, task_id: str, payload: Dict[str, Any]):
        vertex = PhysicalExecutionVertex(task_id, payload)
        with self._lock:
            self.vertices.append(vertex)
        return vertex

    def calculate_saturation(self, subsystem_signals: dict):
        # Centralized pressure calculation
        score = sum(subsystem_signals.values()) / len(subsystem_signals) if subsystem_signals else 0.0
        with self._lock:
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
