import unittest
import os
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.constitutional_court.constitutional_court import ConstitutionalCourt
from sarita_runtime.kernel.component_identity.sovereign_identity_engine import SovereignIdentityEngine
from sarita_runtime.kernel.sovereign_trust.certificate_revocation_registry import CertificateRevocationRegistry
from sarita_runtime.kernel.sovereign_constitution.constitutional_runtime_guard import ConstitutionalViolationException

class TrustInfrastructureAttackTest(unittest.TestCase):
    def setUp(self):
        self.engine = SovereignIdentityEngine()
        self.revocation = CertificateRevocationRegistry()
        self.court = ConstitutionalCourt(self.engine, self.revocation)
        # Certify the real one
        self.engine.certify_component("UnifiedExecutionGraph", "sarita_runtime/kernel/runtime_graph/unified_execution_graph.py")

    def test_revoked_identity_attack(self):
        # 1. Component is authorized
        graph = UnifiedExecutionGraph(ledger_db=":memory:", court=self.court)
        graph.emit_event("t1", "OK", {})
        graph.wait_for_convergence()
        self.assertEqual(len(graph.get_all_vertices()), 1)

        # 2. Revoke identity
        self.revocation.revoke("UnifiedExecutionGraph", "Security breach simulation.")

        # 3. Attempt mutation with revoked identity
        graph.emit_event("t2", "ATTACK", {})

        # Convergence should complete with NO new vertices because the worker blocked the mutation
        graph.wait_for_convergence(timeout=2)
        self.assertEqual(len(graph.get_all_vertices()), 1)

        graph.shutdown()

    def test_quarantined_identity_attack(self):
        # 1. Quarantine component
        self.revocation.quarantine("UnifiedExecutionGraph", duration=10)

        graph = UnifiedExecutionGraph(ledger_db=":memory:", court=self.court)
        graph.emit_event("t3", "ATTACK", {})

        graph.wait_for_convergence(timeout=2)
        self.assertEqual(len(graph.get_all_vertices()), 0)
        graph.shutdown()

if __name__ == "__main__":
    unittest.main()
