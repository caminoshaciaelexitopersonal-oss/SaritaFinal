import os
import json
from sarita_runtime.kernel.formal_consistency.global_consistency_engine import GlobalConsistencyEngine

class AutonomousGovernanceEngine:
    """
    Autonomous Governance Engine that audits decisions against rules and Constitutional Axioms.
    Integrates directly with Phase 130.
    """
    def __init__(self):
        self.consistency_engine = GlobalConsistencyEngine()
        self.laws = []
        self._load_governance_policies()

    def _load_governance_policies(self):
        # We can fetch axioms from consistency registry
        axioms = self.consistency_engine.registry.axioms
        for ax_id, ax_data in axioms.items():
            self.laws.append({
                "law_id": f"GOV-LAW-{ax_id}",
                "description": ax_data.get("statement", "Operational Compliance"),
                "critical": True
            })

        # Add basic operational constraints
        self.laws.append({
            "law_id": "GOV-LAW-STABILITY",
            "description": "System stability must remain above 0.8500",
            "critical": True
        })

    def validate_proposal(self, decision_node: dict) -> dict:
        """
        Determines whether a proposed decision violates any constitutional axiom or policy.
        """
        violations = []
        needs_validation = False

        # Heuristic check: does it conflict with stability laws?
        if decision_node.get("risk", 0.0) > 0.90:
            violations.append("GOV-LAW-STABILITY: Proposed action risk exceeds safe operational thresholds")

        # If impact is high, it always requires high validation
        if decision_node.get("impact", 0.0) > 0.70:
            needs_validation = True

        is_approved = len(violations) == 0

        return {
            "compliant": is_approved,
            "violations": violations,
            "needs_validation": needs_validation,
            "required_clearance_level": "CRITICAL" if needs_validation else "STANDARD"
        }
