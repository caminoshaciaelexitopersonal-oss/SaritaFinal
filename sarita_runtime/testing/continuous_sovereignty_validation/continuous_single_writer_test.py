import unittest
import threading
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class ContinuousSingleWriterTest(unittest.TestCase):
    def test_concurrent_emissions(self):
        graph = UnifiedExecutionGraph(ledger_db=":memory:")
        num_threads = 10
        events_per_thread = 100

        def producer(tid):
            for i in range(events_per_thread):
                graph.emit_event(f"t_{tid}_{i}", "CONCURRENT_TEST", {"data": i})

        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=producer, args=(i,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        graph.wait_for_convergence()

        # Verify all events captured
        vertices = graph.get_all_vertices()
        self.assertEqual(len(vertices), num_threads * events_per_thread)

        # Verify linear hash chain integrity
        for i in range(1, len(vertices)):
            self.assertEqual(vertices[i].payload['parent_hash'], vertices[i-1].vertex_hash)

        graph.shutdown()

if __name__ == "__main__":
    unittest.main()
