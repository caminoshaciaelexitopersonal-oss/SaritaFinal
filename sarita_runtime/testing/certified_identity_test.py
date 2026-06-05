import unittest
import os
import queue
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.constitutional_court.constitutional_court import ConstitutionalCourt
from sarita_runtime.kernel.component_identity.sovereign_identity_engine import SovereignIdentityEngine
from sarita_runtime.kernel.sovereign_constitution.constitutional_runtime_guard import ConstitutionalViolationException

class CertifiedIdentityTest(unittest.TestCase):
    def test_certified_mutation_allow(self):
        engine = SovereignIdentityEngine()
        court = ConstitutionalCourt(engine)

        # Certify the graph component
        graph_file = "sarita_runtime/kernel/runtime_graph/unified_execution_graph.py"
        engine.certify_component("UnifiedExecutionGraph", graph_file)

        graph = UnifiedExecutionGraph(ledger_db=":memory:", court=court)
        graph.emit_event("t1", "TEST", {})
        graph.wait_for_convergence()

        self.assertEqual(len(graph.get_all_vertices()), 1)
        graph.shutdown()

    def test_certified_mutation_reject(self):
        engine = SovereignIdentityEngine()
        court = ConstitutionalCourt(engine)

        # Do NOT certify the component
        graph = UnifiedExecutionGraph(ledger_db=":memory:", court=court)
        graph.emit_event("t1", "TEST", {})

        # In this test, the worker processes the event, fails validation,
        # logs the error, calls task_done(), and continues.
        # So it DOES converge, but with 0 vertices.
        graph.wait_for_convergence(timeout=2)

        self.assertEqual(len(graph.get_all_vertices()), 0)
        graph.shutdown()

if __name__ == "__main__":
    unittest.main()
