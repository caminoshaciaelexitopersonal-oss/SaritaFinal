import unittest
import logging
import time
from sarita_runtime.kernel.runtime_cortex.sovereign_cortex import SovereignCortex
from sarita_runtime.kernel.sovereign_enforcement_fabric import SovereignEnforcementFabric
from sarita_runtime.kernel.hardware_authority.physical_resource_authority import PhysicalResourceAuthority
from sarita_runtime.kernel.io_uring_fabric.io_uring_execution_engine import IoUringExecutionEngine

class TestCoreConvergence(unittest.TestCase):
    def setUp(self):
        self.cortex = SovereignCortex()
        self.graph = self.cortex.nervous_system
        self.graph.ledger.db_path = "/tmp/test_convergence.db"
        self.graph.ledger._init_db()
        self.enforcement = SovereignEnforcementFabric(self.graph)
        self.hardware = self.enforcement.hardware_authority

    def test_scenario_1_telemetry_to_ledger(self):
        """Telemetry -> Graph -> Decision"""
        self.cortex.process_telemetry_signal("thermal", "TEMPERATURE", 0.95)
        self.graph.wait_for_convergence()
        self.assertTrue(self.graph.global_pressure > 0.8)

        # Verify the throttling decision vertex specifically
        vertices = self.graph.get_all_vertices()
        throttling_vertex = next((v for v in vertices if v.payload['action'] == "EXTREME_PRESSURE_THROTTLING"), None)
        self.assertIsNotNone(throttling_vertex)

    def test_scenario_2_irq_authority(self):
        """IRQ -> Graph -> PhysicalResourceAuthority"""
        self.enforcement.claim_hardware_path("NIC_0", 16, 2)
        self.graph.wait_for_convergence()
        self.assertEqual(self.hardware.irq_assignments[16], 2)
        self.assertEqual(self.graph.ownership["IRQ_16"], "2")

    def test_scenario_5_io_path(self):
        """IO Request -> Graph -> io_uring -> CQE"""
        res = self.enforcement.execute_material_io("task_123", "READ", {"fd": 5})
        self.assertGreaterEqual(res, 0)
        self.graph.wait_for_convergence()

        vertices = self.graph.get_all_vertices()
        self.assertTrue(any(v.payload['action'] == "IO_SUBMISSION" for v in vertices))
        self.assertTrue(any(v.payload['action'] == "IO_COMPLETION" for v in vertices))

if __name__ == "__main__":
    unittest.main()
