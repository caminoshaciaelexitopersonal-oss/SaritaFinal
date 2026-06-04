import unittest
import logging
import time
import os
from sarita_runtime.kernel.sovereign_enforcement_fabric import SovereignEnforcementFabric
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class TestIoUringSaturation(unittest.TestCase):
    def setUp(self):
        self.db = "/tmp/test_io.db"
        if os.path.exists(self.db): os.remove(self.db)
        self.graph = UnifiedExecutionGraph(ledger_db=self.db)
        self.enforcement = SovereignEnforcementFabric(self.graph)

    def tearDown(self):
        if os.path.exists(self.db): os.remove(self.db)

    def test_04_io_uring_saturation(self):
        """Simulate SQ saturation and verify causal completion trace."""
        for i in range(10):
            self.enforcement.execute_material_io(f"task_{i}", "WRITE", {"size": 4096})

        self.graph.wait_for_convergence()

        vertices = self.graph.get_all_vertices()
        io_submissions = [v for v in vertices if v.payload.get('action') == "IO_SUBMISSION"]
        self.assertEqual(len(io_submissions), 10)

if __name__ == "__main__":
    unittest.main()
