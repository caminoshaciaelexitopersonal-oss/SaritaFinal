import unittest
import time
import os
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class TestIrqStorm(unittest.TestCase):
    def test_01_irq_saturation(self):
        db = "/tmp/test_irq.db"
        if os.path.exists(db): os.remove(db)
        graph = UnifiedExecutionGraph(ledger_db=db)
        for i in range(5):
            graph.update_ownership(f"IRQ_{i}", str(i))
        graph.wait_for_convergence()
        self.assertGreater(len(graph.get_all_vertices()), 4)
        if os.path.exists(db): os.remove(db)

if __name__ == "__main__":
    unittest.main()
