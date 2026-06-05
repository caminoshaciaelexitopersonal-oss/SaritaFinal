import unittest
import threading
import time
import queue
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class QueueOverflowTest(unittest.TestCase):
    def test_queue_backpressure_potential(self):
        # Current queue is unbounded. We simulate an overflow risk by flooding
        # and checking memory/time.
        graph = UnifiedExecutionGraph(ledger_db=":memory:")

        # Suspend event processing by pausing the worker if possible,
        # or just flooding faster than it can process.
        print("Flooding unbounded queue...")
        start_time = time.time()
        for i in range(50000):
            graph.emit_event(f"t_{i}", "FLOOD", {"data": "A" * 100})

        q_size = graph._event_queue.qsize()
        print(f"Queue size after flood: {q_size}")

        # Verify it can still converge
        graph.wait_for_convergence(timeout=30)
        end_time = time.time()
        print(f"Converged after flood in {end_time - start_time:.2f}s")

        self.assertEqual(len(graph.get_all_vertices()), 50000)
        graph.shutdown()

if __name__ == "__main__":
    unittest.main()
