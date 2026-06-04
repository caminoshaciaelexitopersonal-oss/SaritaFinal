import unittest
import time
import os
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.invariant_engine.runtime_invariant_engine import GraphInvariantValidator

class TestGraphCorruption(unittest.TestCase):
    def test_missing_vertex_detection(self):
        db = "/tmp/graph_test.db"
        if os.path.exists(db): os.remove(db)
        graph = UnifiedExecutionGraph(ledger_db=db)
        graph.update_ownership("CPU", "0")
        graph.update_ownership("CPU", "1")
        graph.wait_for_convergence()

        # Simular corrupción en memoria del grafo
        self.assertGreater(len(graph.vertices), 0)
        graph.vertices.pop(0)

        valid, msg = GraphInvariantValidator.validate_causality(graph)
        self.assertFalse(valid)
        self.assertIn("Causal break", msg)
        if os.path.exists(db): os.remove(db)

    def test_duplicate_id_rejection(self):
        graph = UnifiedExecutionGraph()
        from sarita_runtime.kernel.runtime_graph.physical_execution_vertex import PhysicalExecutionVertex
        v = PhysicalExecutionVertex("task", {"action": "TEST"})
        graph.vertices.append(v)
        graph.vertices.append(v)

        valid, msg = GraphInvariantValidator.validate_unicity(graph)
        self.assertFalse(valid)
        self.assertIn("Duplicate decision ID", msg)

if __name__ == "__main__":
    unittest.main()
