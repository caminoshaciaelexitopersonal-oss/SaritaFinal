import logging
from typing import List
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.evidence_fabric.evidence_constitution import EvidenceConstitution
from sarita_runtime.kernel.replay_fabric.state_equivalence_validator import StateEquivalenceValidator
from sarita_runtime.kernel.replay_fabric.replay_evidence_comparator import ReplayEvidenceComparator

class GraphInvariantValidator:
    @staticmethod
    def validate_causality(graph: UnifiedExecutionGraph):
        vertices = graph.get_all_vertices()
        if not vertices: return True, "Empty Graph"
        expected_parent = "0" * 64
        for v in vertices:
            if v.payload.get('parent_hash') != expected_parent:
                return False, f"Causal break at vertex {v.vertex_id}"
            expected_parent = v.payload.get('ledger_hash')
        return True, "CAUSALITY_VERIFIED"

    @staticmethod
    def validate_unicity(graph: UnifiedExecutionGraph):
        vertices = graph.get_all_vertices()
        ids = [v.vertex_id for v in vertices]
        if len(ids) != len(set(ids)):
            return False, "Duplicate decision ID detected"
        return True, "UNICITY_VERIFIED"

class LedgerInvariantValidator:
    @staticmethod
    def validate_persistence(graph: UnifiedExecutionGraph, ledger):
        valid, msg = ledger.verify_integrity()
        if not valid: return False, msg
        vertices = graph.get_all_vertices()
        count = ledger.get_entry_count()
        if count != len(vertices):
            return False, f"Ledger count ({count}) mismatch with Graph vertices ({len(vertices)})"
        return True, "PERSISTENCE_VERIFIED"

class RuntimeInvariantEngine:
    """
    Sovereign Invariant Engine (Phase 77).
    REFACTORED PHASE 77.4A: Expanded with replay equivalence verification.
    """
    def __init__(self, graph: UnifiedExecutionGraph):
        self.graph = graph
        self.ledger = graph.ledger

    def perform_full_audit(self):
        logging.info("Invariant Engine: Performing full system audit.")
        results = {}
        results['graph_causality'] = GraphInvariantValidator.validate_causality(self.graph)
        results['graph_unicity'] = GraphInvariantValidator.validate_unicity(self.graph)
        results['ledger_persistence'] = LedgerInvariantValidator.validate_persistence(self.graph, self.ledger)
        all_passed = all(r[0] for r in results.values())
        return all_passed, results

    def verify_replay_equivalence(self, replayed_graph):
        """Phase 77.4A: Verifies absolute equivalence with a replayed state."""
        passed_state, state_checks = StateEquivalenceValidator.validate_equivalence(self.graph, replayed_graph)
        passed_evidence, evidence_msg = ReplayEvidenceComparator.compare_vertices(self.graph, replayed_graph)

        return (passed_state and passed_evidence), {
            "state_checks": state_checks,
            "evidence": evidence_msg
        }
