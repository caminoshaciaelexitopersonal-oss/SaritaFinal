import unittest
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class TestIrqStorm(unittest.TestCase):
    def test_01_irq_saturation(self):
        graph = UnifiedExecutionGraph()
        for i in range(5):
            graph.update_ownership(f"IRQ_{i}", str(i))
        self.assertGreater(len(graph.get_all_vertices()), 4)

if __name__ == "__main__":
    unittest.main()
