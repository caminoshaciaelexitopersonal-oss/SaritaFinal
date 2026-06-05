import unittest
import os
import time
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class CryptographicResilienceValidator(unittest.TestCase):
    def test_hash_chain_uniqueness(self):
        db_path = "/tmp/crypto_resilience.db"
        if os.path.exists(db_path): os.remove(db_path)

        graph = UnifiedExecutionGraph(ledger_db=db_path)
        count = 1000
        for i in range(count):
            graph.emit_event("t1", "PING", {"i": i})

        graph.wait_for_convergence()
        vertices = graph.get_all_vertices()

        # Verify all hashes are unique
        hashes = [v.vertex_hash for v in vertices]
        self.assertEqual(len(set(hashes)), count, "Hash collision detected!")

        # Verify chain integrity
        for i in range(1, len(vertices)):
            self.assertEqual(vertices[i].payload['parent_hash'], vertices[i-1].vertex_hash)

        print(f"Verified chain integrity for {count} vertices.")
        graph.shutdown()
        if os.path.exists(db_path): os.remove(db_path)

if __name__ == "__main__":
    unittest.main()
