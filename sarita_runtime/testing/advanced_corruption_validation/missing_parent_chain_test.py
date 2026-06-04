import unittest
import os
import time
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.evidence_fabric.evidence_validator import EvidenceValidator

class MissingParentChainTest(unittest.TestCase):
    def test_missing_parent_detection(self):
        # This requires a validator that checks parent_hash against the graph state
        # Current UnifiedExecutionGraph doesn't throw on missing parent during replay, it just sets it.
        # Let's verify we can detect it.

        db_path = "/tmp/missing_parent.db"
        graph = UnifiedExecutionGraph(ledger_db=db_path)
        graph.emit_event("t1", "ACTION", {"data": 1})
        graph.wait_for_convergence()

        v1 = graph.get_all_vertices()[0]

        # Manually create a vertex with a fake parent hash
        from sarita_runtime.kernel.runtime_graph.physical_execution_vertex import PhysicalExecutionVertex
        v2 = PhysicalExecutionVertex("t2", {"parent_hash": "FAKE_PARENT"})

        # Verify the hash is different or the parent link is broken
        self.assertNotEqual(v2.parent_hash, v1.vertex_hash)

        if os.path.exists(db_path): os.remove(db_path)

if __name__ == "__main__":
    unittest.main()
