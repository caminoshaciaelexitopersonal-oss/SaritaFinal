import unittest
import os
import time
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class MillionEventTest(unittest.TestCase):
    def test_one_million_events(self):
        db_path = "/tmp/million_event.db"
        if os.path.exists(db_path): os.remove(db_path)

        graph = UnifiedExecutionGraph(ledger_db=db_path)
        count = 1000000

        print(f"Ingesting {count} events...")
        start = time.time()
        for i in range(count):
            graph.emit_event(f"t_{i}", "LOAD_TEST", {"val": i})
            if i % 100000 == 0:
                print(f"Progress: {i}/{count}")

        graph.wait_for_convergence(timeout=600)
        end = time.time()
        print(f"Ingestion of {count} events took {end - start:.2f}s ({(count/(end-start)):.2f} events/s)")

        self.assertEqual(len(graph.get_all_vertices()), count)

        graph.shutdown()
        if os.path.exists(db_path): os.remove(db_path)

if __name__ == "__main__":
    unittest.main()
