import unittest
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.constitutional_guard.constitutional_guard_engine import SingleWriterGuard

class ConstitutionalEnforcementTest(unittest.TestCase):
    def test_single_writer_protection(self):
        # We need to add the check to a mutation-prone area.
        # Let's mock a direct mutation attempt.

        def simulate_rogue_mutation():
            SingleWriterGuard.validate_caller()

        with self.assertRaises(PermissionError):
            simulate_rogue_mutation()

    def test_authorized_context(self):
        # This is harder to test without a real call from the worker thread,
        # but we can verify the validator logic.
        class MockGraph:
            def _process_event_batch(self):
                return SingleWriterGuard.validate_caller()

        m = MockGraph()
        self.assertTrue(m._process_event_batch())

if __name__ == "__main__":
    unittest.main()
