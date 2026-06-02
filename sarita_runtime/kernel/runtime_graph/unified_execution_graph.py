import logging
import threading
import json
import queue
from typing import Dict, Any, List
from sarita_runtime.kernel.runtime_graph.physical_execution_vertex import PhysicalExecutionVertex
from sarita_runtime.kernel.runtime_ledger.sovereign_audit_ledger import SovereignAuditLedger

class UnifiedExecutionGraph:
    """
    Unified Execution Graph (Phase 76).
    The SINGLE system nervous system with Single Writer Sovereignty.
    """
    def __init__(self):
        self._lock = threading.Lock()
        self.vertices = []
        self.ownership = {}
        self.global_pressure = 0.0
        self.active_epoch = 0
        self.material_runqueue = []
        self.completed_tasks = set()
        self._last_vertex_hash = "0" * 64

        # Ledger for persistence
        self.ledger = SovereignAuditLedger()

        # Event system for causal writing
        self._event_queue = queue.Queue()
        self._worker_thread = threading.Thread(target=self._event_processor, daemon=True)
        self._worker_thread.start()

    def emit_event(self, task_id: str, action: str, payload: dict):
        """Standard public entry point for all system events."""
        self._event_queue.put({
            "task_id": task_id,
            "action": action,
            "payload": payload
        })

    def _event_processor(self):
        """Single Writer Thread: The ONLY one that modifies the graph state and vertices."""
        while True:
            event = self._event_queue.get()
            try:
                self._process_material_event(event)
            except Exception as e:
                logging.error(f"Graph: Event processing failed: {e}")
            finally:
                self._event_queue.task_done()

    def _process_material_event(self, event: dict):
        task_id = event['task_id']
        action = event['action']
        payload = event['payload']

        with self._lock:
            # 1. Update State based on Action
            if action == "OWNERSHIP_CHANGE":
                self.ownership[payload['resource']] = payload['owner']
            elif action == "PRESSURE_UPDATE":
                self.global_pressure = payload['score']
            elif action == "TASK_AUTHORIZED":
                self.material_runqueue.append(payload['task'])
            elif action == "EXECUTION_COMPLETE":
                self.completed_tasks.add(task_id)
            elif action == "EPOCH_ADVANCE":
                self.active_epoch = payload['new_epoch']

            # 2. Register persistent vertex
            vertex_payload = payload.copy()
            vertex_payload['action'] = action
            vertex_payload['previous_hash'] = self._last_vertex_hash

            vertex = PhysicalExecutionVertex(task_id, vertex_payload)
            vertex.execution_epoch = self.active_epoch
            vertex.vertex_hash = vertex._calculate_material_hash()

            self.vertices.append(vertex)
            self._last_vertex_hash = vertex.vertex_hash

            # 3. Automatic Ledger Persistence (Single Authority flow)
            self.ledger.record_vertex(vertex)

            logging.debug(f"Graph: Materialized vertex and ledger for {action} on {task_id}")

    # --- Read-Only Sovereign API ---

    def get_next_authorized_task(self):
        with self._lock:
            if self.material_runqueue:
                return self.material_runqueue.pop(0)
        return None

    def get_vertex(self, task_id: str):
        with self._lock:
            for v in reversed(self.vertices):
                if v.task_id == task_id:
                    return v
        return None

    def get_all_vertices(self):
        with self._lock:
            return list(self.vertices)

    # --- Legacy/Convenience Proxies (Now emitting events) ---

    def register_material_decision(self, task_id: str, action: str, evidence: dict):
        self.emit_event(task_id, action, evidence)
        return None

    def update_ownership(self, resource: str, owner_id: str):
        self.emit_event(f"owner_{resource}", "OWNERSHIP_CHANGE", {"resource": resource, "owner": owner_id})

    def calculate_saturation(self, subsystem_signals: dict):
        score = sum(subsystem_signals.values()) / len(subsystem_signals) if subsystem_signals else 0.0
        self.emit_event("system", "PRESSURE_UPDATE", {"signals": subsystem_signals, "score": score})
        return score

    def add_authorized_task(self, task: Dict[str, Any]):
        self.emit_event(task.get('id', 'unknown'), "TASK_AUTHORIZED", {"task": task})

    def mark_execution_complete(self, task_id: str):
        self.emit_event(task_id, "EXECUTION_COMPLETE", {})
