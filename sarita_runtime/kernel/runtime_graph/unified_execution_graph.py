import logging
import threading
import json
import queue
import time
from typing import Dict, Any, List
from sarita_runtime.kernel.runtime_graph.physical_execution_vertex import PhysicalExecutionVertex
from sarita_runtime.kernel.runtime_ledger.sovereign_audit_ledger import SovereignAuditLedger
from sarita_runtime.kernel.evidence_fabric.evidence_constitution import EvidenceConstitution
from sarita_runtime.kernel.constitutional_guard.constitutional_guard_engine import SingleWriterGuard

class UnifiedExecutionGraph:
    """
    Unified Execution Graph (Phase 77).
    The SINGLE system nervous system with Single Writer Sovereignty.
    """
    def __init__(self, ledger_db=":memory:"):
        self._lock = threading.RLock() # Reentrant lock for safe internal calls
        self.vertices = []
        self.ownership = {}
        self.global_pressure = 0.0
        self.active_epoch = 0
        self.material_runqueue = []
        self.completed_tasks = set()
        self._last_ledger_hash = "0" * 64

        self.ledger = SovereignAuditLedger(ledger_db)
        self._event_queue = queue.Queue()
        self._running = True
        self._worker_thread = threading.Thread(target=self._event_processor, name="GraphEventProcessor", daemon=True)
        self._worker_thread.start()

    def shutdown(self):
        """Cleanly shuts down the graph worker thread."""
        self._running = False
        self._event_queue.put(None) # Sentinel to wake up and stop
        self._worker_thread.join(timeout=5)
        logging.info("UnifiedExecutionGraph: Operational shutdown complete.")

    def emit_event(self, task_id: str, action: str, payload: dict):
        self._event_queue.put({
            "task_id": task_id,
            "action": action,
            "payload": payload
        })

    def wait_for_convergence(self, timeout=120):
        """Helper for tests to ensure the single writer has processed all events and any consequential events."""
        start = time.time()
        while True:
            if self._event_queue.empty():
                time.sleep(0.1) # Grace period for consequential events
                if self._event_queue.empty():
                    # Double check tasks are done processing
                    if self._event_queue.unfinished_tasks == 0:
                        break
            if time.time() - start > timeout:
                # Log state to help debug
                logging.error(f"Convergence Timeout. Queue empty: {self._event_queue.empty()}, Vertices: {len(self.vertices)}")
                raise TimeoutError("Graph convergence timed out")
            time.sleep(0.02)

    def _event_processor(self):
        BATCH_SIZE = 500
        while self._running:
            events = []
            shutdown_detected = False
            try:
                # Get at least one event
                event = self._event_queue.get(timeout=0.01)
                if event is None:
                    shutdown_detected = True
                else:
                    events.append(event)

                # Fill batch
                if not shutdown_detected:
                    while len(events) < BATCH_SIZE:
                        try:
                            next_event = self._event_queue.get_nowait()
                            if next_event is None:
                                shutdown_detected = True
                                break
                            events.append(next_event)
                        except queue.Empty:
                            break
            except queue.Empty:
                continue

            try:
                if events:
                    self._process_event_batch(events)
            except Exception as e:
                logging.error(f"Graph: Batch processing failed: {e}")
            finally:
                for _ in range(len(events)):
                    self._event_queue.task_done()
                if shutdown_detected:
                    if not events or events[-1] is not None:
                         # Handle case where None was the trigger but not in events or not the last
                         pass
                    self._event_queue.task_done() # Done for the None sentinel
                    break

    def _process_event_batch(self, events: List[dict]):
        # The guard will check if we are in this function
        with self._lock:
            vertices_to_record = []
            for event in events:
                task_id = event['task_id']
                action = event['action']
                payload = event['payload']

                is_replay = 'ledger_hash' in payload and 'payload' in payload
                target_payload = payload['payload'] if is_replay else payload

                # 1. Update State
                if action == "OWNERSHIP_CHANGE":
                    self.ownership[target_payload['resource']] = target_payload['owner']
                elif action == "PRESSURE_UPDATE":
                    score = target_payload.get('score')
                    self.global_pressure = score if score is not None else 0.0
                elif action == "TASK_AUTHORIZED":
                    self.material_runqueue.append(target_payload.get('task', {}))
                elif action == "EXECUTION_COMPLETE":
                    self.completed_tasks.add(task_id)
                elif action == "SET_NUMA_AFFINITY":
                    self.ownership[f"MEM_{task_id}"] = f"NUMA_{target_payload.get('node')}"

                # 2. Construct Vertex
                if is_replay:
                    vertex = PhysicalExecutionVertex(task_id, target_payload, vertex_id=payload.get('vertex_id'))
                    vertex.payload = payload
                    vertex.vertex_hash = payload['ledger_hash']
                    vertex.execution_epoch = payload['epoch_id']
                    self._last_ledger_hash = vertex.vertex_hash
                else:
                    vertex = PhysicalExecutionVertex(task_id, target_payload)
                    evidence_data = {
                        "decision_id": vertex.vertex_id,
                        "vertex_id": vertex.vertex_id,
                        "epoch_id": self.active_epoch,
                        "telemetry_hash": EvidenceConstitution.calculate_subsystem_hash(target_payload.get('telemetry', {})),
                        "ownership_hash": EvidenceConstitution.calculate_subsystem_hash(self.ownership),
                        "execution_hash": EvidenceConstitution.calculate_subsystem_hash({"q_len": len(self.material_runqueue)}),
                        "parent_hash": self._last_ledger_hash,
                        "timestamp": time.time(),
                        "action": action,
                        "payload": target_payload
                    }
                    evidence_data["ledger_hash"] = EvidenceConstitution.calculate_subsystem_hash(evidence_data)
                    vertex.payload = evidence_data
                    vertex.vertex_hash = evidence_data["ledger_hash"]
                    self._last_ledger_hash = vertex.vertex_hash
                    vertices_to_record.append(vertex)

                self.vertices.append(vertex)

            if vertices_to_record:
                self.ledger.record_vertices_batch(vertices_to_record)


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

    # --- Legacy Proxies ---

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
