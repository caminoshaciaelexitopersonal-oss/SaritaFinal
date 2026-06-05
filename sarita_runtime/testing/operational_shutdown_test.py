import unittest
import threading
import time
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.scheduling_fabric.sovereign_scheduler import SovereignScheduler

class OperationalShutdownCertification(unittest.TestCase):
    def test_clean_operational_shutdown(self):
        graph = UnifiedExecutionGraph(ledger_db=":memory:")
        scheduler = SovereignScheduler(graph)

        scheduler.start_physical_dispatch()
        graph.emit_event("test", "PING", {})
        graph.wait_for_convergence()

        # Verify threads are running
        thread_names = [t.name for t in threading.enumerate()]
        self.assertIn("GraphEventProcessor", thread_names)
        self.assertIn("SchedulerDispatch", thread_names)

        # Shutdown
        scheduler.shutdown()
        graph.shutdown()

        # Verify threads are gone
        time.sleep(0.5)
        thread_names_after = [t.name for t in threading.enumerate()]
        self.assertNotIn("GraphEventProcessor", thread_names_after)
        self.assertNotIn("SchedulerDispatch", thread_names_after)

if __name__ == "__main__":
    unittest.main()
