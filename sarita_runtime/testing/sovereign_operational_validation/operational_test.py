import unittest
import logging
import json
import time
import os
from sarita_runtime.kernel.runtime_cortex.sovereign_cortex import SovereignCortex
from sarita_runtime.kernel.sovereign_enforcement_fabric import SovereignEnforcementFabric
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class TestOperationalSovereignty(unittest.TestCase):
    def setUp(self):
        self.db_path = "/tmp/test_operational.db"
        if os.path.exists(self.db_path): os.remove(self.db_path)
        self.graph = UnifiedExecutionGraph(ledger_db=self.db_path)
        self.cortex = SovereignCortex(graph=self.graph)
        self.enforcement = SovereignEnforcementFabric(self.graph)

    def tearDown(self):
        if os.path.exists(self.db_path): os.remove(self.db_path)

    def test_case_1_telemetry_flow(self):
        """Telemetry -> Graph -> Scheduler -> Enforcement -> Ledger (Audit Lineage)"""
        self.cortex.process_telemetry_signal("thermal", "PRESSURE", 0.9)
        self.graph.wait_for_convergence()
        self.assertGreater(self.graph.global_pressure, 0.8)

        vertices = self.graph.get_all_vertices()
        decisions = [v.payload['action'] for v in vertices if v.task_id == "system"]
        self.assertIn("EXTREME_PRESSURE_THROTTLING", decisions)

    def test_case_2_irq_flow(self):
        """IRQ -> Enforcement -> Graph (Ownership)"""
        self.enforcement.claim_hardware_path("NVME_DISK", 32, 4)
        self.graph.wait_for_convergence()
        self.assertEqual(self.graph.ownership["IRQ_32"], "4")

    def test_case_5_io_uring_flow(self):
        """io_uring -> CQE -> Ledger (Graph)"""
        self.enforcement.execute_material_io("io_task_1", "WRITE", {"fd": 10})
        self.graph.wait_for_convergence()

        vertices = self.graph.get_all_vertices()
        self.assertTrue(any(v.payload['action'] == "IO_SUBMISSION" for v in vertices if v.task_id == "io_task_1"))
        self.assertTrue(any(v.payload['action'] == "IO_COMPLETION" for v in vertices if v.task_id == "io_task_1"))

    def test_case_6_replay_determinism(self):
        """Ledger (Graph Vertices) -> Replay -> Reconstruction"""
        self.cortex.process_telemetry_signal("cpu", "PRESSURE", 0.5)
        self.enforcement.claim_hardware_path("NIC", 24, 1)
        self.graph.wait_for_convergence()

        original_vertices = self.graph.get_all_vertices()
        original_ownership = dict(self.graph.ownership)
        original_pressure = self.graph.global_pressure

        # Sim Replay
        replayed_graph = UnifiedExecutionGraph(ledger_db=":memory:")
        for v in original_vertices:
            replayed_graph.emit_event(v.task_id, v.payload['action'], v.payload)

        replayed_graph.wait_for_convergence()

        self.assertEqual(len(replayed_graph.get_all_vertices()), len(original_vertices))
        self.assertEqual(replayed_graph.ownership, original_ownership)
        self.assertEqual(replayed_graph.global_pressure, original_pressure)

if __name__ == "__main__":
    unittest.main()
